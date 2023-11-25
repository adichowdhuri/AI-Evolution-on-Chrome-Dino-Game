from pdb import runcall
import pygame
import neat
import math
import os
import sys
import random

speed_shift = 30

pygame.init()

#global consts
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun1.png"),
           pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun2.png") ]

DUCKING = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck1.png"), 
            pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck2.png")]

JUMPING = pygame.image.load(r'AI-Evolution-on-Chrome-Dino-Game\images\DinoJump.png')

SMALL_CACTUS = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus1.png"),
                pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus2.png"),
                pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus3.png")]

LARGE_CACTUS = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus1.png"),
                pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus2.png"),
                pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus3.png")]

BIRD = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\Bird1.png"), 
            pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\Bird2.png")]

CLOUD = pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\Cloud.png")
            
BG = pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\Track.png")

FONT = pygame.font.Font('freesansbold.ttf', 20)

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5 

    def __init__(self, img = RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0
    
    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8 + (speed_shift / 100)
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING[self.step_index // 5]
        self.rect.x = self.X_POS 
        self.rect.y = self.Y_POS + 32
        self.step_index += 1
    
    def release_duck(self):
        self.dino_duck = False
    
    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        for obstacle in obstacles:
            pygame.draw.line(SCREEN, self.color, (self.rect.x + 54, self.rect.y + 12), obstacle.rect.center, 2)


class Obstacle:
    def __init__ (self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0

    
    def update(self):
        self.rect.x -= game_speed
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        if not isinstance(self, Bird):
            SCREEN.blit(self.image[self.type], self.rect)
            pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        else:       
            self.image = BIRD[self.step_index // 5]
            SCREEN.blit(self.image, self.rect)
            pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)

class SmallCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, 1)
        self.rect.y = 270

class HighBird(Bird):
    def __init__(self, image):
        super().__init__(image, 0)
        self.rect.y = 220  # Higher position

class LowBird(Bird):
    def __init__(self, image):
        super().__init__(image, 0)
        self.rect.y = 300  # Lower position


def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a-pos_b
    dy = pos_a-pos_b
    return math.sqrt(dx**2+dy**2)

def eval_genomes(genomes, config):
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs,ge, nets, points
    clock = pygame.time.Clock()
    points = 0

    obstacles = []
    dinosaurs = []
    ge = []
    nets = []

    x_pos_bg = 0
    y_pos_bg = 380
    game_speed = 20 + speed_shift

    for genome_id, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = FONT.render(f'score:  {str(points)}', True, (0, 0, 0))
        SCREEN.blit(text, (950, 50))


    def statistics():
        global dinosaurs, game_speed, ge
        text_1 = FONT.render(f'Dinosaurs Alive:  {str(len(dinosaurs))}', True, (0, 0, 0))
        text_2 = FONT.render(f'Generation:  {pop.generation+1}', True, (0, 0, 0))
        text_3 = FONT.render(f'Game Speed:  {str(game_speed)}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50, 480))
        SCREEN.blit(text_3, (50, 510))



    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill((255,255,255))

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(SCREEN)

        if len(dinosaurs) == 0:
           break

        if len(obstacles) == 0:
            # if points > 1000:
            #     rand_int = random.randint(0, 3)
            # else:
            #     rand_int = random.randint(0, 1)
            rand_int = random.randint(0, 3)
            if rand_int == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, random.randint(0, 2)))
            elif rand_int == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, random.randint(0, 2)))
            elif rand_int == 2:
                obstacles.append(LowBird(BIRD))
            elif rand_int == 3:
                obstacles.append(HighBird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            for i, dinosaur in enumerate(dinosaurs):
               if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    remove(i)

        #user_input = pygame.key.get_pressed()

        for i, dinosaur in enumerate(dinosaurs):
            obstacle_type = -1  # Initialize to an invalid value
            if isinstance(obstacle, SmallCactus):
                obstacle_type = 0
            elif isinstance(obstacle, LargeCactus):
                obstacle_type = 1
            elif isinstance(obstacle, LowBird):
                obstacle_type = 2
            elif isinstance(obstacle, HighBird):
                obstacle_type = 3

            output = nets[i].activate((dinosaur.rect.y,
                                       obstacle.rect.x,
                                       obstacle.rect.y,
                                       obstacle_type
                                    ))

            # Decision to jump
            if output[0] > 0.5 and (dinosaur.rect.y == dinosaur.Y_POS or dinosaur.rect.y == (dinosaur.Y_POS + 32)):
                dinosaur.dino_jump = True
                dinosaur.dino_run = False
                dinosaur.dino_duck = False

            # Decision to duck
            elif output[1] > 0.5 and dinosaur.rect.y == dinosaur.Y_POS:
                dinosaur.dino_jump = False
                dinosaur.dino_run = False
                dinosaur.dino_duck = True

            # Decision to stop ducking
            elif output[2] > 0.5 and dinosaur.rect.y == (dinosaur.Y_POS + 32):
                dinosaur.release_duck()
                dinosaur.dino_jump = False
                dinosaur.dino_run = True



        statistics()
        score()
        background()
        clock.tick(30)
        pygame.display.update()


#NEAT steup
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
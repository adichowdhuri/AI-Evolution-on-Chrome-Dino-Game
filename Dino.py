import pygame
import random

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
points = 0
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
def load_image(image_path):
    return pygame.image.load(image_path)

RUNNING = [load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun1.png"),
           load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun2.png")]

DUCKING = [load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck1.png"),
           load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck2.png")]

JUMPING = load_image(r'AI-Evolution-on-Chrome-Dino-Game\images\DinoJump.png')

SMALL_CACTUS = [load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus1.png"),
                load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus2.png"),
                load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\SmallCactus3.png")]

LARGE_CACTUS = [load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus1.png"),
                load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus2.png"),
                load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\LargeCactus3.png")]

BIRD = [load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\Bird1.png"),
        load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\Bird2.png")]

CLOUD = load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\Cloud.png")
BG = load_image(r"AI-Evolution-on-Chrome-Dino-Game\images\Track.png")

FONT = pygame.font.Font('freesansbold.ttf', 20)

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img=RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.step_index = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not (self.dino_duck or self.dino_jump):
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            self.rect.y = self.Y_POS

    def duck(self):
        self.image = DUCKING[self.step_index // 5]
        self.rect.y = self.Y_POS + 32
        self.step_index += 1

    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

class Obstacle:
    def __init__(self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

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
        super().__init__(image, number_of_cacti)
        self.rect.y = 250 if number_of_cacti % 2 == 0 else 300  # Randomize bird height

def main():
    global game_speed, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    game_speed = 20
    obstacles = []

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = FONT.render(f'Points:  {str(points)}', True, (0, 0, 0))
        SCREEN.blit(text, (950, 50))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))

        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw(SCREEN)
            if player.rect.colliderect(obstacle.rect):
                run = False

        if len(obstacles) == 0 or obstacles[-1].rect.x < 500:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, random.randint(0, 2)))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, random.randint(0, 2)))
            else:
                obstacles.append(Bird(BIRD, random.randint(0, 1)))

        user_input = pygame.event.get()
        player.update(user_input)
        player.draw(SCREEN)

        score()
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()

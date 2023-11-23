import pygame

from DinoAI import SCREEN_WIDTH, Dinosaur

pygame.init()

#GLOBAL CONSTS
SCREEN_HEIGHTS = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHTS))

RUNNING = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun1.png"), 
            pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoRun2.png")]

JUMPING = pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoJump.png")
DUCKING = [pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck1.png"), 
            pygame.image.load(r"AI-Evolution-on-Chrome-Dino-Game\images\DinoDuck2.png")]

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

class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_jump = False
        self.dino_run = True

        self.step_index = 0
        self.img = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dimo_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_duck = True
            self.dino_run = False
        elif not(self.dino_duck or self.dino_jump):
            self.dino_run = True

        def run(self):
            self.image = self.run_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1

def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        SCREEN.fill((255,255,255))
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)
        clock.tick(30)

main()
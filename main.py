import  pygame
import sys

pygame.init()
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Break Breaker')
clock = pygame.time.Clock()
FPS = 60
speed = 0

bg = pygame.image.load("assets/images/bg.png")


ball_img = pygame.image.load('assets/images/ball.png')
paddle_img = pygame.image.load('assets/images/paddle.png')
rectangle_img = pygame.image.load('assets/images/rectangle.png')

ambient_sound = pygame.mixer.Sound('assets/sounds/ambient_sound.mp3')
touched_bar_sound = pygame.mixer.Sound('assets/sounds/touched_bar.mp3')
touched_brick_sound = pygame.mixer.Sound('assets/sounds/touched_brick.mp3')

class Padle(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6

def run_game(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit


#if __name__ == '__main__':
#    main.()
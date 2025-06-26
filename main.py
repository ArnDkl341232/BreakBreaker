import  pygame

pygame.init()
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Break Breaker')
clock = pygame.time.Clock()
FPS = 60
speed = 0

bg = pygame.image.load("./assets/images/bg.png")

ball_img = pygame.image.load('assets/images/ball.png')
paddle_img = pygame.image.load('assets/images/paddle.png')
rectangle_img = pygame.image.load('assets/images/rectangle.png')

ambient_sound = pygame.mixer.Sound('assets/sounds/ambient_sound.mp3')
touched_bar_sound = pygame.mixer.Sound('assets/sounds/touched_bar.mp3')
touched_brick_sound = pygame.mixer.Sound('assets/sounds/touched_brick.mp3')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scr.blit(bg, (0,0))
    scr.blit(paddle_img, (50,100))
    scr.blit(rectangle_img, (200,300))
    scr.blit(ball_img, (400,300))
    pygame.display.update()


class Padle(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6



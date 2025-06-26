import pygame

pygame.init()
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Break Breaker')
clock = pygame.time.Clock()
FPS = 60
speed = 6

WIDTH = 800
HEIGHT = 600

# Loading assets
bg = pygame.image.load("./assets/images/bg.png")
ball_img = pygame.image.load('assets/images/ball.png')
paddle_img = pygame.image.load('assets/images/paddle.png')
rectangle_img = pygame.image.load('assets/images/rectangle.png')

ambient_sound = pygame.mixer.Sound('assets/sounds/ambient_sound.mp3')
touched_bar_sound = pygame.mixer.Sound('assets/sounds/touched_bar.mp3')
touched_brick_sound = pygame.mixer.Sound('assets/sounds/touched_brick.mp3')

# === Paddle Class ===
class Paddle:
    def __init__(self, x, y):
        self.image = paddle_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# === Ball Class ===
class Ball:
    def __init__(self, posx, posy, radius, speed):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.xFac = 1
        self.yFac = -1
        self.firstTime = 1
        self.rect = ball_img.get_rect(center=(self.posx, self.posy))

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac
        self.rect.center = (self.posx, self.posy)

        # Bounce vertically
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        # Bounce horizontally (dont work right now)
#        if self.posx <= 0 and self.firstTime:
#            self.firstTime = 0
#            return 1
#        elif self.posx >= WIDTH and self.firstTime:
#            self.firstTime = 0
#            return -1
#        return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def draw(self, surface):
        surface.blit(ball_img, self.rect)

# Create paddle instance
paddle = Paddle(x=WIDTH // 2 - paddle_img.get_width() // 2, y=HEIGHT - 50)
ball = Ball(posx=400, posy=300, radius=10, speed=5)

# === Game Loop ===
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scr.blit(bg, (0, 0))

    # Update and draw objects
    paddle.move()
    paddle.draw(scr)

    ball.update()
    ball.draw(scr)

    # Draw other stuff (example brick)     ((BRIK HEIGHT 30PX ====== BRIK WIDTH 63PX))
    brik1 = scr.blit(rectangle_img, (50, 50))
    brik5 = scr.blit(rectangle_img, (113, 50))
    brik6 = scr.blit(rectangle_img, (176, 50))
    brik7 = scr.blit(rectangle_img, (239, 50))


    brik2 = scr.blit(rectangle_img, (50, 80))


    brik3 = scr.blit(rectangle_img, (50, 110))


    brik4 = scr.blit(rectangle_img, (50, 140))


    pygame.display.update()

pygame.quit()

import pygame

pygame.init()
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Break Breaker')
clock = pygame.time.Clock()
FPS = 60
speed = 12

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
        self.rect = ball_img.get_rect(center=(posx, posy))

    def update(self, paddle):
        # Move the ball
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac
        self.rect.center = (self.posx, self.posy)

        # Bounce off top
        if self.posy - self.radius <= 0:
            self.yFac *= -1

        # Fell off bottom after reset
        if self.posy - self.radius > HEIGHT:
            self.reset()

        # Bounce off left/right walls
        if self.posx - self.radius <= 0 or self.posx + self.radius >= WIDTH:
            self.xFac *= -1

        # Bounce off paddle
        if self.yFac > 0 and self.rect.colliderect(paddle.rect):
            self.yFac *= -1
            touched_bar_sound.play()

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
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

    # Updating and drawing objects
    paddle.move()
    paddle.draw(scr)

    ball.update(paddle)
    ball.draw(scr)

    # Draw of Briks     ((BRIK HEIGHT 30PX ====== BRIK WIDTH 63PX))
    brik1 = scr.blit(rectangle_img, (50, 50))
    brik5 = scr.blit(rectangle_img, (113, 50))
    brik6 = scr.blit(rectangle_img, (176, 50))
    brik7 = scr.blit(rectangle_img, (239, 50))
    brik8 = scr.blit(rectangle_img, (302, 50))
    brik9 = scr.blit(rectangle_img, (365, 50))
    brik10 = scr.blit(rectangle_img, (428, 50))
    brik11 = scr.blit(rectangle_img, (491, 50))
    brik12 = scr.blit(rectangle_img, (554, 50))
    brik13 = scr.blit(rectangle_img, (617, 50))
    brik14 = scr.blit(rectangle_img, (680, 50))

#####################################################################

    brik2 = scr.blit(rectangle_img, (50, 80))
    brik15 = scr.blit(rectangle_img, (113, 80))
    brik16 = scr.blit(rectangle_img, (176, 80))
    brik17= scr.blit(rectangle_img, (239, 80))
    brik18 = scr.blit(rectangle_img, (302, 80))
    brik19 = scr.blit(rectangle_img, (365, 80))
    brik20 = scr.blit(rectangle_img, (428, 80))
    brik21 = scr.blit(rectangle_img, (491, 80))
    brik22 = scr.blit(rectangle_img, (554, 80))
    brik23 = scr.blit(rectangle_img, (617, 80))
    brik24 = scr.blit(rectangle_img, (680, 80))

#####################################################################

    brik3 = scr.blit(rectangle_img, (50, 110))
    brik25 = scr.blit(rectangle_img, (113, 110))
    brik26 = scr.blit(rectangle_img, (176, 110))
    brik27 = scr.blit(rectangle_img, (239, 110))
    brik28 = scr.blit(rectangle_img, (302, 110))
    brik29 = scr.blit(rectangle_img, (365, 110))
    brik30 = scr.blit(rectangle_img, (428, 110))
    brik31 = scr.blit(rectangle_img, (491, 110))
    brik32 = scr.blit(rectangle_img, (554, 110))
    brik33 = scr.blit(rectangle_img, (617, 110))
    brik34 = scr.blit(rectangle_img, (680, 110))

#####################################################################

    brik4 = scr.blit(rectangle_img, (50, 140))
    brik35 = scr.blit(rectangle_img, (113, 140))
    brik36 = scr.blit(rectangle_img, (176, 140))
    brik37 = scr.blit(rectangle_img, (239, 140))
    brik38 = scr.blit(rectangle_img, (302, 140))
    brik39 = scr.blit(rectangle_img, (365, 140))
    brik40 = scr.blit(rectangle_img, (428, 140))
    brik41 = scr.blit(rectangle_img, (491, 140))
    brik42 = scr.blit(rectangle_img, (554, 140))
    brik43 = scr.blit(rectangle_img, (617, 140))
    brik44 = scr.blit(rectangle_img, (680, 140))

#####################################################################

    pygame.display.update()

pygame.quit()

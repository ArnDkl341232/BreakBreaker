import pygame
import random
import math

pygame.init()
scr = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 72)
FPS = 60

#assets
bg = pygame.image.load("./assets/images/bg.png")
ball_img = pygame.image.load('assets/images/ball.png')
paddle_img = pygame.image.load('assets/images/paddle.png')

rectangle_img = pygame.image.load('assets/images/rectangle.png')
touched_bar_sound   = pygame.mixer.Sound('assets/sounds/touched_bar.mp3')
touched_brick_sound = pygame.mixer.Sound('assets/sounds/touched_brick.mp3')

# Generate brick
brick_rects = []
rows, cols = 4, 11
x0, y0 = 50, 50
x_placing = rectangle_img.get_width()
y_placing = rectangle_img.get_height()
for row in range(rows):
    for col in range(cols):
        x = x0 + col * x_placing
        y = y0 + row * y_placing
        brick_rects.append(rectangle_img.get_rect(topleft=(x, y)))

# Paddle
class Paddle:
    def __init__(self, x, y, speed):
        self.image = paddle_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  and self.rect.left  > 0:       self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:     self.rect.x += self.speed
    def draw(self):
        scr.blit(self.image, self.rect.topleft)

# Ball
class Ball:
    def __init__(self, x, y, speed):
        self.image = ball_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.vx = 0  # Initialize velocities
        self.vy = 0
        self.active = True
        self.reset_position(x, y)

    def reset_position(self, x, y):
        # Called only on initial spawn
        self.rect.center = (x, y)
        angle = random.uniform(-0.5, 0.5)  # slight horizontal angle in radians
        self.vx = self.speed * math.sin(angle)
        self.vy = -self.speed * math.cos(angle)

    def reset(self, paddle):
        self.rect.center = (paddle.rect.centerx, paddle.rect.top - self.rect.height)
        self.active = False
        angle = random.uniform(-0.5, 0.5)
        self.vx = self.speed * math.sin(angle)
        self.vy = -self.speed * math.cos(angle)

    def update(self, paddle):
        if not self.active:
            self.rect.centerx = paddle.rect.centerx
            return

        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)

        # Wall collision
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.vx *= -1
        if self.rect.top <= 0:
            self.vy *= -1

        # Bottom of screen = reset
        if self.rect.top > 600:
            self.reset(paddle)

        # Paddle collision
        if self.vy > 0 and self.rect.colliderect(paddle.rect):
            touched_bar_sound.play()
            hit_pos = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
            max_angle = 60
            angle = hit_pos * math.radians(max_angle)
            self.vx = self.speed * math.sin(angle)
            self.vy = -self.speed * math.cos(angle)

    def draw(self):
        scr.blit(self.image, self.rect.topleft)


#Our configs of game
paddle = Paddle( (800 - paddle_img.get_width())//2, 550, speed=8 ) #for first level will be 6ball and 8 for padle
ball   = Ball(400, 300, speed=10)


running = True
while running:
    clock.tick(FPS)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not ball.active:
                ball.active = True

    scr.blit(bg, (0, 0))
    paddle.move()
    paddle.draw()
    ball.update(paddle)
    ball.draw()

#brik breaking
    if ball.active:
        for rect in brick_rects[:]:
            if ball.rect.colliderect(rect):
                brick_rects.remove(rect)
                touched_brick_sound.play()
                ball.vy *= -1
                break

    # Draw bricks
    if not brick_rects:
        win_text = font.render("YOU WIN!", True, (255, 255, 0))
        text_rect = win_text.get_rect(center=(400, 300))
        scr.blit(win_text, text_rect)
        # Stop ball and paddle
        ball.active = False
    else:
        for rect in brick_rects:
            scr.blit(rectangle_img, rect.topleft)

    pygame.display.flip()

pygame.quit()

import  pygame

pygame.init()
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Break Breaker')
clock = pygame.time.Clock()
FPS = 60
speed = 0

HEIGHT = 800
WIDTH = 600

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

    scr.blit(rectangle_img, (200,300))
    scr.blit(ball_img, (400,300))
    pygame.display.update()


class Padle(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        scr.blit(paddle_img, (50, 100))
        self.image = image
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = +10
            scr.blit()
        if keys[pygame.K_RIGHT] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x = -10
            scr.blit()

class Ball:
    def __init__(self, posx, posy, radius, speed):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.xFac = 1
        self.yFac = -1
        self.ball = scr.blit(ball_img, (400, 300))


    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ball

    class Striker:
        def __init__(self, posx, posy, width, height, speed):
            self.posx = posx
            self.posy = posy
            self.width = width
            self.height = height
            self.speed = speed
            # Rect that is used to control the position and collision of the object
            self.geekRect = pygame.Rect(posx, posy, width, height)
            # Object that is blit on the screen
            self.geek = scr.blit(rectangle_img, (200,300))

        # Used to display the object on the screen
        def display(self):
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

        def update(self, yFac):
            self.posy = self.posy + self.speed * yFac

            # Restricting the striker to be below the top surface of the screen
            if self.posy <= 0:
                self.posy = 0
            # Restricting the striker to be above the bottom surface of the screen
            elif self.posy + self.height >= HEIGHT:
                self.posy = HEIGHT - self.height

            # Updating the rect with the new values
            self.geekRect = (self.posx, self.posy, self.width, self.height)

        def displayScore(self, text, score, x, y, color):
            text = font20.render(text + str(score), True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)

            screen.blit(text, textRect)

        def getRect(self):
            return self.geekRect


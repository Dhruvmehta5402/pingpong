import sys, pygame, random
import time

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


class LeftPaddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./paddle.png')
        self.image = pygame.transform.scale(self.image, (20, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (15, 250)
        self.totalLives = 5

class RightPaddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./paddle.png')
        self.image = pygame.transform.scale(self.image, (20, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (485, 250)
        self.totalLives = 5

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./circle.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (255, 250)

leftpad = LeftPaddle()
rightpad = RightPaddle()
ball = Ball()

paddles = pygame.sprite.Group()
paddles.add(leftpad)
paddles.add(rightpad)

balls = pygame.sprite.Group()
balls.add(ball)

toQuit = 0
clock = pygame.time.Clock()
ballspeed = [2, 3]
while 1:
    clock.tick(60)
    screen.fill((0,0,0))
    paddles.draw(screen)
    balls.draw(screen)
    myFont = pygame.font.SysFont("Times New Roman", 18)
    numsLivesDraw = myFont.render(str(leftpad.totalLives), True, (250, 250, 250))
    numsLivesDrawRight = myFont.render(str(rightpad.totalLives), True, (250, 250, 250))
    screen.blit(numsLivesDraw, (30,30))
    screen.blit(numsLivesDrawRight, (400,30))
    if leftpad.totalLives <= 0 or rightpad.totalLives <= 0:
        letter = pygame.font.SysFont("Times New Roman", 30)
        message = 'Game Over'
        gameOver = letter.render(message, True, (250, 250, 250))
        screen.blit(gameOver, (150,100))
        toQuit = 1
        
    pygame.display.flip()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if leftpad.rect.top > 5:
            leftpad.rect = leftpad.rect.move([0, -5])
    if key[pygame.K_s]:
        if leftpad.rect.bottom < 495:
            leftpad.rect = leftpad.rect.move([0, 5])

    if key[pygame.K_UP]:
        if rightpad.rect.top > 5:
            rightpad.rect = rightpad.rect.move([0, -5])
    if key[pygame.K_DOWN]:
        if rightpad.rect.bottom < 495:
            rightpad.rect = rightpad.rect.move([0, 5])

    if ball.rect.top <= 5:
        ballspeed[1] = ballspeed[1] * -1
    if ball.rect.bottom >= 495:
        ballspeed[1] = ballspeed[1] * -1

    if ball.rect.left <= 0:
        leftpad.totalLives = leftpad.totalLives -1
        ball.rect.center = (250, 250)
        ballspeed = [2, 4]
        time.sleep(1)
    if ball.rect.right >= 500:
        rightpad.totalLives = rightpad.totalLives -1
        ball.rect.center = (250, 250)
        ballspeed = [-2, 4]
        time.sleep(1)

    leftcollide = pygame.sprite.spritecollideany(leftpad, balls)
    rightcollide = pygame.sprite.spritecollideany(rightpad, balls)
    if leftcollide != None:
        ballspeed[0] = ballspeed[0] * -1
        ballspeed[0] = ballspeed[0] + 0.5
    if rightcollide != None:
        ballspeed[0] = ballspeed[0] * -1
        ballspeed[0] = ballspeed[0] - 0.5
    ball.rect = ball.rect.move(ballspeed)
    
    if toQuit == 1:
        time.sleep(5)
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
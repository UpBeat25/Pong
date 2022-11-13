import pygame
import random
pygame.init()
wl, wb = 1000, 600
window = pygame.display.set_mode((wl, wb))

pygame.display.set_caption("Pong")  # You can set a custom name

FPS = 60

speed = 5

f = random.randint(1, 2)

dead = False

WHITE = (255, 255, 255)

# player 1
x1, y1 = 10, 300
player1 = pygame.Rect(x1, y1, 10, 40)
score1 = 0
# player 2
x2, y2 = 980, 300
player2 = pygame.Rect(x2, y2, 10, 40)
score2 = 0
# ball
xb, yb = 500, 300
a, b = 3, 3
ball = pygame.draw.circle(window, (255, 255, 255), (xb, yb), 5)

line = pygame.Rect(500, 0, 1, wl)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    font = pygame.font.Font(None, 150)
    text = font.render(str(score1), True, WHITE)
    window.blit(text, (250, 10))

    text2 = font.render(str(score2), True, WHITE)
    window.blit(text2, (700, 10))

    if f == 1:
        xb += a
        yb += b
    else:
        xb -= a
        yb -= b

    player1 = pygame.Rect(x1, y1, 10, 40)
    player2 = pygame.Rect(x2, y2, 10, 40)
    ball = pygame.draw.circle(window, (255, 255, 255), (xb, yb), 5)

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_w] and y1 >= 0:
        y1 -= speed
    if userInput[pygame.K_s] and y1 <= 560:
        y1 += speed
    if userInput[pygame.K_UP] and y2 >= 0:
        y2 -= speed
    if userInput[pygame.K_DOWN] and y2 <= 560:
        y2 += speed

    if yb <= 0 or yb >= 600:
        b *= -1

    if xb <= 0 or xb >= 1000:
        dead = True

    if xb <= 0:
        score2 += 1
    if xb >= 1000:
        score1 += 1

    if dead is True:
        f = random.randint(1, 2)
        x1, y1 = 10, 300
        x2, y2 = 980, 300
        xb, yb = 500, 300
        a, b = 3, 3
        dead = False

    if pygame.Rect.colliderect(ball, player1) or pygame.Rect.colliderect(ball, player2):
        a *= -1

    pygame.draw.rect(window, (255, 255, 255), player1)
    pygame.draw.rect(window, (255, 255, 255), player2)
    pygame.draw.rect(window, (255, 255, 255), line)
    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()

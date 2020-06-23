import pygame, random
from random import randrange

#screen
window = pygame.display.set_mode((1920, 1060))
FPS = 60
clock = pygame.time.Clock()
running = True

#images
images = []

for i in range(1):
    image = pygame.image.load("background.jpg")
    images.append(image)

main_background = 0

#wins
wins = []

for k in range(3):
    win = pygame.image.load("win" + str(k) + ".jpg")
    wins.append(win)

random_number = randrange(3)
win = 2


while running:
    clock.tick(FPS)
    window.blit(images[main_background], (0, 0))
    pygame.display.update()

    if random_number == 0 and win == 0:
        window.blit(wins[win], (480, 400))
        pygame.display.update()
    elif random_number == 1 and win == 1:
        window.blit(wins[win], (480, 400))
        pygame.display.update()
    elif random_number == 2 and win == 2:
        window.blit(wins[win], (480, 400))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_SPACE:
                pos = pygame.mouse.get_pos()
                print(pos)


print(random_number)
pygame.quit()
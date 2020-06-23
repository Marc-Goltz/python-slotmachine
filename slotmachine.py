import pygame, random
from random import randrange

#screen
pygame.init()
window = pygame.display.set_mode((1920, 1060))
FPS = 60
clock = pygame.time.Clock()
running = True

cash = 1000


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


win = 0


while running:
    clock.tick(FPS)
    window.blit(images[main_background], (0, 0))
    font = pygame.font.SysFont("arial", 30, True)
    text = font.render("CASH: $" + str(cash), 1, (255, 255, 255))
    text2 = font.render("E", 1, (255, 255, 255))
    window.blit(text, (17, 26))
    if cash >= 75:
        if win == 0:
            window.blit(wins[win], (570, 600))

        elif win == 1:
            window.blit(wins[win], (570, 600))
        elif win == 2:
            window.blit(wins[win], (570, 600))

        pygame.display.update()

    else:

        text1 = font.render("NOT ENOUGH MONEY PRESS " + "e" + " TO GET MONEY!", 1, (245, 133, 73))
        window.blit(text1, (595, 650))
        pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cash -= 75
            if event.key == pygame.K_e:
                cash += 25



print(win)
pygame.quit()
import pygame
import random

width = 600
height = 800
black = (0,0,0)
white = (255,255,255)
green = (64, 255, 0)

control_x = 0
control_y = 0

pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
rectangleImg = pygame.image.load('rectangle.png')

def square(x, y, color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, 40-1, 40-1))


def background():
    x = 0
    y = 0
    while x != 440:
        pygame.draw.rect(gameDisplay, white, pygame.Rect(x, 0, 1, 800))
        x += 40
    while y != 800:
        pygame.draw.rect(gameDisplay, (184,184,184), pygame.Rect(0, y, 400, 1))
        y += 40
    pygame.draw.rect(gameDisplay, (184,184,184), pygame.Rect(0, 799, 400, 1))


def keyboardInput(event):
    global control_x
    global control_y
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        control_y -= 1
    if pressed[pygame.K_s]:
        control_y += 1
    if pressed[pygame.K_a]:
        control_x -= 1
    if pressed[pygame.K_d]:
        control_x += 1
     
        
def rectangle(x,y):
    print((x,y))
    gameDisplay.blit(rectangleImg, (x,y))


def main():
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
            keyboardInput(event)

        gameDisplay.fill((8, 8, 8))
        background()
        #rectangle(x,y)
        square(40+1,40+1,(255, 0, 0))
        pygame.display.update()
        clock.tick(60) 

if __name__ == "__main__":
    main()
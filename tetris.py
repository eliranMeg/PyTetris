# אורי יראש חביתה
import pygame
import random

####control panel####
width = 600
height = 800
control_x = 0
control_y = 0
#####################

black = (0,0,0)
white = (255,255,255)
hight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

colors = [(8, 8, 8), (64, 255, 0), (7, 6, 147), (255, 103, 0), (249, 7, 0), (109, 7, 252), (64, 198, 255), (239, 25, 252)]
shapes = {1:[(4,0), (4,1), (4,2), (4,3)],
          2:[(4,0), (4,1), (5,1), (6,1)],
          3:[(4,1), (5,1), (6,1), (6,0)],
          4:[(4,0), (4,1), (5,0), (5,1)],
          5:[(4,1), (5,1), (5,0), (6,0)],
          6:[(4,0), (5,0), (5,1), (6,1)],
          7:[(4,1), (5,1), (5,0), (6,1)]}
number_shape = 2
board = list()


pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
rectangleImg = pygame.image.load('rectangle.png')


def draw_sahpe_on_board():
    global board
    global number_shape
    global control_x
    global control_y
    for i in (shapes[number_shape]):
        board[i[-1] + control_y][i[0]] = number_shape

def print_board():
    global board
    print("\n#########################")
    for row in board:
        print(row)
    print("#########################")


def read_board():
    global board
    for row in range(0, 20):
        for index in range(0, 10):
            if not(board[row][index] == 0):
                square(index, row, colors[board[row][index]])

def change_automatic_shape():
    global board
    global number_shape
    global control_y

    for i in (shapes[number_shape]):
        board[i[-1]][i[0]] = 0

def square(x, y, color):
    pygame.draw.rect(gameDisplay, color, pygame.Rect(x*40+1, y*40+1, 40-1, 40-1))


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
    global number_shape
    global control_x
    global control_y
    pressed = pygame.key.get_pressed()
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
    i = 0
    flag = True
    global board
    global control_y
    for i in range(0,20):
        board.append([0,0,0,0,0,0,0,0,0,0])

    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                keyboardInput(event)
        gameDisplay.fill((8, 8, 8))
        background()
        if flag:
            draw_sahpe_on_board()
        if i == 60:
            flag = False
            control_y += 1
            change_automatic_shape()
            i = 0
        print(control_y)
        read_board()
        print_board()

        pygame.display.update()
        i += 1
        clock.tick(60)

if __name__ == "__main__":
    main()
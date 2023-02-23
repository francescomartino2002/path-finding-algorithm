import pygame
import finder
import  sys
from threading import Thread

start = (17,17)
goal = (2,2)

#window settings
WIDTH = 600
HEIGHT = 600
MARGIN = 3
BLOCK_SIZE = (WIDTH / 20) - MARGIN
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (93, 63, 211)

#map initialization
dim = 20
map = [ [0]*dim for _ in range(dim) ]
map[start[0]][start[1]] = 4
map[goal[0]][goal[1]] = 4


pygame.init()
pygame.display.set_caption('A* Pathfinder')

screen = pygame.display.set_mode((WIDTH, HEIGHT))

t1 = Thread(target = finder.main, args=(map,))

def draw_Grid():
    for row in range(20):
        for column in range(20):
            color = white
            if map[row][column] == 1:
                color = black
            elif map[row][column] == 2:
                color = red
            elif map[row][column] == 3:
                color = green
            elif map[row][column] == 4:
                color = purple
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + BLOCK_SIZE) * column + MARGIN,
                              (MARGIN + BLOCK_SIZE) * row + MARGIN,
                              BLOCK_SIZE,
                              BLOCK_SIZE])


while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                t1.start()
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        X = (pos[1]*dim) // WIDTH
        Y = (pos[0]*dim) // HEIGHT
        map[X][Y] = 1

    screen.fill(black)
    draw_Grid()   
    pygame.display.update()


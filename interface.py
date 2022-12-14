import pygame
import pygame.locals
from mapa import Mapa

#   Initialize th pygame
pygame.init()

#size of matrix * pixels
lines = 7
rows = 10
size = width, height = 64*rows, 64*lines
screen = pygame.display.set_mode(size)

# Title and icon
pygame.display.set_caption("VectorRace")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)




# Desenha o Mapa
def drawMap(screen):
    mapa = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,1,1,0],
        [0,1,1,1,1,1,1,1,1,3],
        [0,2,1,1,0,0,0,1,1,3],
        [0,1,1,1,1,1,1,1,1,3],
        [0,0,0,0,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
    colors = [pygame.Color("black"), pygame.Color("grey"), pygame.Color("green"), pygame.Color("red")]
    for r in range(lines):
        for c in range(rows):
            pygame.draw.rect(screen, colors[mapa[r][c]], pygame.Rect(c*64, r*64, 64, 64))
            



# Player
playerImg = pygame.image.load('racecar.png')
playerImg = pygame.transform.rotate(playerImg, 270)
playerX = 1*64
playerY = 3*64

def player():
    screen.blit(playerImg,(playerX,playerY))


    


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False 
    
    # Background colour
    screen.fill((50, 50, 50))

    drawMap(screen)
    player()
    pygame.display.update()




#coordinates = [(x, y) for x in range(10) for y in range(5)]

   
    
    
    #coordinates = [(x, y) for x in range(10) for y in range(7)]


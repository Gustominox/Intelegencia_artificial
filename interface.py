import pygame
import pygame.locals
from mapa import Mapa
from player import Player
from vector import Vector
#   Initialize th pygame
pygame.init()

#size of matrix * pixels
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
SCALE = 128

# Title and icon
pygame.display.set_caption("VectorRace")
icon = pygame.image.load('imgs/icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('imgs/racecar.png')
playerImg = pygame.transform.rotate(playerImg, 270)




# Desenha o Mapa
def drawMap(screen,mapa):
    content = mapa.content
    colors = [pygame.Color("black"), pygame.Color("grey"), pygame.Color("green"), pygame.Color("red")]
    for line in range(mapa.lines):
        for row in range(mapa.rows):
            pygame.draw.rect(screen, colors[content[line][row]], pygame.Rect(row*SCALE, line*SCALE, SCALE, SCALE))
            
def player(player):
    playerX = player.estado.x * SCALE
    playerY = player.estado.y * SCALE
    screen.blit(playerImg,(playerX,playerY))

def movePlayer(Player):
    
    


# Game Loop
running = True

mapa = Mapa("tracks/track.txt")
jogador = Player(Vector(1,3))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False 
    
    # Background colour
    screen.fill((50, 50, 50))

    drawMap(screen,mapa)
    player(jogador)
    pygame.display.update()




#coordinates = [(x, y) for x in range(10) for y in range(5)]

   
    
    
    #coordinates = [(x, y) for x in range(10) for y in range(7)]


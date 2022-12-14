import pygame
import pygame.locals
from mapa import Mapa
from player import Player
from vector import Vector


#  Initialize th pygame
pygame.init()

# Cria display do tamanho do ecra
monitor_size = pygame.display.Info()
size = monitor_size.current_w, monitor_size.current_h
screen = pygame.display.set_mode(size)

# Scale usada dependendo do tamanho do ecra
SCALE = 100
SCALEX=136.6
SCALEY=109.71428571428571

# Title and icon
pygame.display.set_caption("VectorRace")
icon = pygame.image.load('imgs/icon.jpg')
pygame.display.set_icon(icon)

# Game States
game_menu = "main_menu"

# Introduz texto para o menu
def drawText (text, font, text_col, x, y):
    texto = font.render(text, True, text_col)
    screen.blit(texto, (x, y))

# Player
playerImg = pygame.image.load('imgs/racecar.png')
playerImg = pygame.transform.rotate(playerImg, 270)
playerImg = pygame.transform.scale(playerImg, (SCALEX,SCALEY))




# Desenha o Mapa
def drawMap(screen,mapa):

    MAP_SCALE_X = monitor_size.current_w/mapa.rows
    MAP_SCALE_Y = monitor_size.current_h/mapa.lines
    #MAP_SCALE = 128

    content = mapa.content
    colors = [pygame.Color("black"), pygame.Color("grey"), pygame.Color("green"), pygame.Color("red")]
    for line in range(mapa.lines):
        for row in range(mapa.rows):
            pygame.draw.rect(screen, colors[content[line][row]], pygame.Rect(row*MAP_SCALE_X, line*MAP_SCALE_Y, MAP_SCALE_X, MAP_SCALE_Y))

            
            
def drawPlayer(player):
    x = player.estado.x * SCALEX
    y = player.estado.y * SCALEY
    #declive = Vector.to_polar(player.velociade)
    #playerImg = pygame.transform.rotate(playerImg, declive)
    screen.blit(playerImg,(x,y))
    

#def movePlayer(Player):
    
    


# Game Loop
# running = True

# mapa = Mapa("tracks/track.txt")
# jogador = Player(Vector(1,3))


# while running:

#     # Background colour
#     screen.fill((50, 50, 50))

#     #CHECK MENU

#     if game_menu == "maps":
#         pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/3) -10, (monitor_size.current_h/5) - 2, 105    , 30 ))
#         drawText("Mapa1", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/3, monitor_size.current_h/5)

        

#     if game_menu == 'main_menu':
#         start = pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/2.5) -10, (monitor_size.current_h/4) - 2, 210    , 30 ))
#         drawText("1.Choose Map", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/2.5, monitor_size.current_h/4)

#         quit_game = pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/2.5) -10, (monitor_size.current_h/4) + 50, 210    , 30 ))
#         drawText("Quit", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/2.5, monitor_size.current_h/4 + 50)

    

#     elif game_menu == 'pista':
        
#         jogo = Jogo("tracks/track.txt")

#         jogo.start()

#         drawMap(screen,mapa)
#         player(jogador)
#         drawText("ESC to return", pygame.font.SysFont("arielblack", 40), (255,255,255), 0, 0)

    









#     for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     game_menu = 'main_menu'
#                 if event.key == pygame.K_1:
#                     game_menu = 'pista'

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if start.collidepoint(pygame.mouse.get_pos()):
#                     game_menu = "pista"
#                 if quit_game.collidepoint(pygame.mouse.get_pos()):
#                     running = False


#             if event.type == pygame.QUIT:
#                 running = False 
    
    

    

    


    

#     pygame.display.update()




#todo
# comecar a criacao de menu (ver main)
# implementar escolha de 1 ou 2 jogadores
# escolher que algoritmo usar para cada jogador
# implementar escolha do mapa


#start 
    #varios maps: (opcao de escolher ver o grafo)
        #1 ou 2 jogadores ou 
            #algoritmo jogador1  #algoritmo jogador2
#quit




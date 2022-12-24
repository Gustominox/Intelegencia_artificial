import pygame
import pygame.locals
from mapa import Mapa
from player import Player
from vector import Vector
import time

#  Initialize th pygame
pygame.init()

# Cria display do tamanho do ecra
monitor_size = pygame.display.Info()
size = monitor_size.current_w, monitor_size.current_h
screen = pygame.display.set_mode(size)

# Scale usada dependendo do tamanho do ecra
SCALE = 100
SCALEX = 136.6
SCALEY = 109.71428571428571


# Player
playerImgRaw = pygame.image.load('imgs/racecar.png')
playerImg = pygame.transform.rotate(playerImgRaw, 270)
# playerImg = pygame.transform.scale(playerImg, (SCALEX,SCALEY))

winImg = pygame.image.load('imgs/winner.png')
winImg = pygame.transform.scale(winImg, size)

# Title and icon
pygame.display.set_caption("VectorRace")
icon = pygame.image.load('imgs/icon.jpg')
icon_dimmed = pygame.image.load('imgs/icon_dimmed2.jpg')
icon_dimmed = pygame.transform.scale(icon_dimmed, size)
pygame.display.set_icon(icon)

# Game States
game_menu = "main_menu"

# Introduz texto para o menu


def drawText(text, font, text_col, x, y):
    texto = font.render(text, True, text_col)
    screen.blit(texto, (x, y))


# Desenha o Mapa
def drawMap(screen, mapa, players):

    MAP_SCALE_X = round(monitor_size.current_w/mapa.rows)
    MAP_SCALE_Y = round(monitor_size.current_h/mapa.lines)
    #MAP_SCALE = 128

    content = mapa.content
    colors = [pygame.Color("black"), pygame.Color(
        "grey"), pygame.Color("green"), pygame.Color("red")]
    for line in range(mapa.lines):
        for row in range(mapa.rows):
            pygame.draw.rect(screen, colors[content[line][row]], pygame.Rect(
                row*MAP_SCALE_X, line*MAP_SCALE_Y, MAP_SCALE_X, MAP_SCALE_Y))
    
    for player in players:
        x = player.estado.x * MAP_SCALE_X
        y = (mapa.lines-player.estado.y-1) * MAP_SCALE_Y
        playerImgFinal = pygame.transform.scale(
            playerImg, (MAP_SCALE_X, MAP_SCALE_Y))
        screen.blit(playerImgFinal, (x, y))


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

FONT = pygame.font.SysFont("arielblack", 40)

WIDTH = monitor_size.current_w
HEIGHT = monitor_size.current_h

MENU_BUTTON_X = WIDTH/20
MENU_BUTTON_Y = HEIGHT/4

SPACE_BETWEEN = 60

def createButton(text, number,color):
    
    rect = pygame.draw.rect(screen, color,
                            pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y + number * SPACE_BETWEEN , 400, 50))

    drawText(text, FONT,
             COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + number * SPACE_BETWEEN + 10)
    
    return rect

def createButton2(text, number,color):
    
    rect = pygame.draw.rect(screen, color,
                            pygame.Rect(MENU_BUTTON_X + 420, MENU_BUTTON_Y + number * SPACE_BETWEEN , 400, 50))

    drawText(text, FONT,
             COLOR_WHITE, MENU_BUTTON_X + 420 + 10, MENU_BUTTON_Y + number * SPACE_BETWEEN + 10)
    
    return rect

def drawMapsMenu(selected):
    screen.fill((50, 50, 50))
    
    map1 = createButton("Mapa Default", 0,COLOR_BLACK)
    map2 = createButton("Mapa Circle", 1,COLOR_BLACK)
    map3 = createButton("Mapa Simple", 2,COLOR_BLACK)
    leave = createButton("Leave", 3,COLOR_BLACK)
    
    
    if selected == 0:                        
        map1 = createButton("Mapa Default", 0,COLOR_RED)
    elif selected == 1:
        map2 = createButton("Mapa Circle", 1,COLOR_RED)
    elif selected == 2:
        map3 = createButton("Mapa Simple", 2,COLOR_RED)
    elif selected == 3:
        leave = createButton("Leave", 3,COLOR_RED)
    else:
        pass
        
        
    return map1, map2, map3, leave

def drawJogMenu(selected):
    screen.fill((50, 50, 50))
    
    one = createButton("Um jogador", 0,COLOR_BLACK)
    two = createButton("Dois jogadores", 1,COLOR_BLACK)
    leave = createButton("Leave", 2,COLOR_BLACK)
    
    
    if selected == 0:                        
        one = createButton("Um jogador", 0,COLOR_RED)
    elif selected == 1:
        two = createButton("Dois jogadores", 1,COLOR_RED)
    elif selected == 2:
        leave = createButton("Leave", 2,COLOR_RED)
    else:
        pass
        
        
    return one,two, leave



def drawAlgoritmosMenu(selected,players):
    screen.fill((50, 50, 50))
    
    selected = players[0].alg_selected
    selected2 = players[1].alg_selected
    
    
    a_estrela = createButton("A*", 0,COLOR_BLACK)
    greedybf = createButton("GreedyBF", 1,COLOR_BLACK)
    greedy = createButton("Greedy", 2,COLOR_BLACK)
    bfs = createButton("BFS", 3,COLOR_BLACK)
    dfs = createButton("DFS", 4,COLOR_BLACK)
    
    a_estrela2 = createButton2("A*", 0,COLOR_BLACK)
    greedybf2 = createButton2("GreedyBF", 1,COLOR_BLACK)
    greedy2 = createButton2("Greedy", 2,COLOR_BLACK)
    bfs2 = createButton2("BFS", 3,COLOR_BLACK)
    dfs2 = createButton2("DFS", 4,COLOR_BLACK)
    
    
    leave_alg = createButton("Leave", 5,COLOR_BLACK)

    
    
    if selected == 0:                        
        a_estrela = createButton("A*", 0,COLOR_RED)
    elif selected == 1:
        greedybf = createButton("GreedyBF", 1,COLOR_RED)
    elif selected == 2:
         greedy = createButton("Greedy", 2,COLOR_RED)
    elif selected == 3:
        bfs = createButton("BFS", 3,COLOR_RED)
    elif selected == 4:
        dfs = createButton("DFS", 4,COLOR_RED)
    else:
        pass
    
    if selected2 == 0:                        
        a_estrela2 = createButton2("A*", 0,COLOR_RED)
    elif selected2 == 1:
        greedybf2 = createButton2("GreedyBF", 1,COLOR_RED)
    elif selected2 == 2:
         greedy2 = createButton2("Greedy", 2,COLOR_RED)
    elif selected2 == 3:
        bfs2 = createButton2("BFS", 3,COLOR_RED)
    elif selected2 == 4:
        dfs2 = createButton2("DFS", 4,COLOR_RED)
    else:
        pass
        
        
    return a_estrela, greedybf, greedy, bfs, dfs,a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg

# drawMap(screen, Mapa("tracks/track.txt"), Player(Vector(0,0)))


# def movePlayer(Player):


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


# todo
# comecar a criacao de menu (ver main)
# implementar escolha de 1 ou 2 jogadores
# escolher que algoritmo usar para cada jogador
# implementar escolha do mapa


# start
    # varios maps: (opcao de escolher ver o grafo)
    # 1 ou 2 jogadores ou
    # algoritmo jogador1  #algoritmo jogador2
# quit


from player import Player
from mapa import *
from vector import Vector
from resolver import Resolver
from grafo import Graph
import time
from interface import *

JOGADAS = [
    Vector(-1, -1),
    Vector(-1, 0),
    Vector(0, -1),
    Vector(0, 0),
    Vector(0, 1),
    Vector(1, 0),
    Vector(1, 1),
    Vector(-1, 1),
    Vector(1, -1),
]


class Jogo:

    def __init__(self, trackFile="tracks/trackSimple.txt"):
        self.players = []
        self.mapa = Mapa(trackFile)
        self.fps = 10
        self.run = True

    def proximasJogadas(self, player):
        """Cria tds as possiveis proximas coordenadas a partir do estado e velocidade do jogador

        Returns:
            Player: Jogador sbr o qual se vai criar as coordenadas
        """
        proximasJogadas = []

        for jogada in JOGADAS:
            proximasJogadas.append(player.estado + player.velocidade + jogada)

        return proximasJogadas

    def addPlayer(self, player):
        self.players.append(player)


    def startPYGame(self):

        running = True

        jogo = Jogo()
        res = Resolver()
        g = Graph()
        

        game_menu = "main_menu"

        COLOR_BLACK = (0, 0, 0)
        COLOR_WHITE = (255, 255, 255)
        COLOR_RED = (255, 0, 0)

        FONT = pygame.font.SysFont("arielblack", 40)

        WIDTH = monitor_size.current_w
        HEIGHT = monitor_size.current_h

        MENU_BUTTON_X = WIDTH/20
        MENU_BUTTON_Y = HEIGHT/4

        SPACE_BETWEEN = 60

        while running:

            # Background colour

            # CHECK MENU

            if game_menu == 'maps':

               
                pass
                

            if game_menu == 'main_menu':
                screen.fill((50, 50, 50))

                jogo.run = True

                screen.blit(icon_dimmed, (0, 0))

                start = createButton("Start", 0,COLOR_BLACK)
                maps = createButton("Choose Map", 1,COLOR_BLACK)
                quit_game = createButton("Quit", 2,COLOR_BLACK)


            if game_menu == 'pista':
                ########################################################################

                time.sleep(1)
                if jogo.run:
                
                    jog = res.aestrelaJog(jogador, [Vector(x, y) for x, y
                                                    in self.mapa.finish], g)

                    possivelPosicao = jogador.estado + jogador.velocidade + jog

                    novaPosicao, stopType = g.checkPath(
                        jogador.estado, possivelPosicao)

                    jogador.jogada(jog)

                    nodoType = g.get_node_by_vector(novaPosicao).type

                    if stopType == WALL:
                        jogador.estado = novaPosicao
                        jogador.velocidade = Vector(0, 0)
                    elif stopType == FINISH:
                        jogador.estado = novaPosicao
                        jogador.velocidade = Vector(0, 0)
                    ########################################################################
                drawMap(screen, mapa, jogador)
                drawText("ESC to return", pygame.font.SysFont(
                    "arielblack", 40), COLOR_WHITE, 0, 0)
                if stopType == FINISH:
                    screen.blit(winImg, (0, 0))

                    jogo.run = False

            for event in pygame.event.get():

                if game_menu == "maps":
                    # event keys
                    
                    
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'

                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if map1.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/track.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                            
                            map1 = createButton("Mapa Default", 0,COLOR_RED)
                            map2 = createButton("Mapa Circle", 1,COLOR_BLACK)
                            map3 = createButton("Mapa Simple", 2,COLOR_BLACK)
                            leave = createButton("Leave", 3,COLOR_BLACK)
                            
                
                        if map2.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/trackCircle.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                            
                            map1 = createButton("Mapa Default", 0,COLOR_BLACK)
                            map2 = createButton("Mapa Circle", 1,COLOR_RED)
                            map3 = createButton("Mapa Simple", 2,COLOR_BLACK)
                            leave = createButton("Leave", 3,COLOR_BLACK)
                            
                        if map3.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/trackSimple.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                            
                            map1 = createButton("Mapa Default", 0,COLOR_BLACK)
                            map2 = createButton("Mapa Circle", 1,COLOR_BLACK)
                            map3 = createButton("Mapa Simple", 2,COLOR_RED)
                            leave = createButton("Leave", 3,COLOR_BLACK)
                            
                            
                        if leave.collidepoint(pygame.mouse.get_pos()):
                            game_menu = 'main_menu'
                            


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'

                if game_menu == "main_menu":
                    # event keys
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'
                        if event.key == pygame.K_1:
                            game_menu = 'pista'
                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "pista"
                            screen.fill((50, 50, 50))
                            drawMap(screen, mapa, jogador)
                            drawText("ESC to return", pygame.font.SysFont(
                                "arielblack", 40), COLOR_WHITE, 0, 0)

                        if maps.collidepoint(pygame.mouse.get_pos()):

                            game_menu = "maps"
                            screen.fill((50, 50, 50))
                            
                            map1 = createButton("Mapa Default", 0,COLOR_BLACK)
                            map2 = createButton("Mapa Circle", 1,COLOR_BLACK)
                            map3 = createButton("Mapa Simple", 2,COLOR_BLACK)
                            leave = createButton("Leave", 3,COLOR_BLACK)
                            
                            
                            

                        if quit_game.collidepoint(pygame.mouse.get_pos()):
                            running = False
                if game_menu == "pista":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'
                    
                    
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


def main():

    jogo = Jogo("tracks/trackCircle.txt")

    jogo.startPYGame()


if __name__ == "__main__":
    main()

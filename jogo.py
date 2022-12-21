
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

    def draw(self):
        print(self.mapa)

    def start(self):

        path = []

        res = Resolver()
        jogador = Player(estadoInicial=self.mapa.start)

        self.addPlayer(jogador)

        on = 10 * self.fps
        ctn = True
        g = Graph()

        g.createGraphCartesian(self.mapa)

        while on:

            self.draw()
            time.sleep(1 / self.fps)

            # jog = res.greedyJog(jogador, [Vector(x, y) for x, y
            #  in self.mapa.finish])

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
                on = 1

            if on != 0:
                on -= 1

            # path.append((novaPosicao.x, novaPosicao.y))
            # res.getPltXY(path)
            # self.mapa.show()
            # res.showPath(path, True)

            # time.sleep(1)

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
            screen.fill((50, 50, 50))

            # CHECK MENU

            if game_menu == 'maps':

                map1 = createButton("MAPA DEFAULT", 0)
                
                map2 = pygame.draw.rect(screen, COLOR_BLACK,
                                        pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y + SPACE_BETWEEN, 400, 50))

                drawText("Map2", FONT,
                         COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + SPACE_BETWEEN + 10)

                map3 = pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(
                    MENU_BUTTON_X, MENU_BUTTON_Y + 2 * SPACE_BETWEEN, 400, 50))

                drawText("Map3", FONT,
                         COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + 2 * SPACE_BETWEEN + 10)

            if game_menu == 'main_menu':

                jogo.run = True

                screen.blit(icon_dimmed, (0, 0))

                start = pygame.draw.rect(screen, COLOR_BLACK,
                                         pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y, 400, 50))

                drawText("Start", FONT,
                         COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + 10)

                maps = pygame.draw.rect(screen, COLOR_BLACK,
                                        pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y + SPACE_BETWEEN, 400, 50))

                drawText("Choose Map", FONT,
                         COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + SPACE_BETWEEN + 10)

                quit_game = pygame.draw.rect(screen, COLOR_BLACK, pygame.Rect(
                    MENU_BUTTON_X, MENU_BUTTON_Y + 2 *SPACE_BETWEEN, 400, 50))

                drawText("Quit", FONT,
                         COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + 2 * SPACE_BETWEEN + 10)

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
                            print("MAPA1")
                            mapa = Mapa("tracks/track.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                
                        if map2.collidepoint(pygame.mouse.get_pos()):
                            print("MAPA2")
                            mapa = Mapa("tracks/trackCircle.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                        if map3.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/trackSimple.txt")
                            jogador = Player(estadoInicial=mapa.start)
                            self.addPlayer(jogador)

                            g.createGraphCartesian(mapa)
                            print("MAPA3")
                            


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

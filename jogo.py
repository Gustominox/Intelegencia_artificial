
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
        self.n_players = 0
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
        self.n_players += 1

    def getPlayers(self):
        return [self.players[i] for i in range(self.n_players)]

    def resetPlayers(self, mapa):
        for player in self.players:
            player.estado = mapa.start
            player.velocidade = Vector(0, 0)

    def startPYGame(self):

        running = True

        jogo = Jogo()
        res = Resolver()
        g = Graph()

        map_selected = 0
        mapa = Mapa("tracks/track.txt")

        jogador1 = Player(Vector(0, 0))
        jogador2 = Player(Vector(0, 0))

        jogo.addPlayer(jogador1)
        jogo.addPlayer(jogador2)

        jogo.resetPlayers(mapa)

        g.createGraphCartesian(mapa)

        alg_selected = 0

        players_selected = 0

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

            # CHECK MENU

            if game_menu == 'main_menu':

                # Background colour
                screen.fill((50, 50, 50))

                jogo.run = True

                screen.blit(icon_dimmed, (0, 0))

                start = createButton("Start", 0, COLOR_BLACK)
                maps = createButton("Choose Map", 1, COLOR_BLACK)
                algoritmos = createButton(
                    "Choose Algorithm(s)", 2, COLOR_BLACK)
                players = createButton(
                    "Choose Number of players", 3, COLOR_BLACK)
                quit_game = createButton("Quit", 4, COLOR_BLACK)

            if game_menu == 'pista':
                ########################################################################

                time.sleep(1)
                if jogo.run:
                    for jogador in jogo.getPlayers():
                        ########################################################################
                        
                        alg_selected = jogador.alg_selected
                        
                        print(f"Algoritmo: {alg_selected}")
                        if alg_selected == 0:
                            jog = res.aestrelaJog(jogador, [Vector(x, y) for x, y
                                                            in mapa.finish], g)

                        elif alg_selected == 1:
                            jog = res.gbfJog(jogador, [Vector(x, y) for x, y
                                                       in mapa.finish], g)

                        elif alg_selected == 2:
                            jog = res.greedyJog(jogador, [Vector(x, y) for x, y
                                                          in mapa.finish])

                        elif alg_selected == 3:
                            jog = res.bfsJog(jogador, [Vector(x, y) for x, y
                                                       in mapa.finish], g)

                        elif alg_selected == 4:
                            jog = res.dfsJog(jogador, [Vector(x, y) for x, y
                                                       in mapa.finish], g)

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
                drawMap(screen, mapa, jogo.getPlayers())
                drawText("ESC to return", pygame.font.SysFont(
                    "arielblack", 40), COLOR_WHITE, 0, 0)

                if stopType == FINISH:
                    screen.blit(winImg, (0, 0))
                    jogo.run = False

            for event in pygame.event.get():

                if game_menu == "maps":

                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if map1.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/track.txt")

                            map_selected = 0
                            map1, map2, map3, leave = drawMapsMenu(
                                map_selected)

                        elif map2.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/trackCircle.txt")

                            map_selected = 1
                            map1, map2, map3, leave = drawMapsMenu(
                                map_selected)

                        elif map3.collidepoint(pygame.mouse.get_pos()):
                            mapa = Mapa("tracks/trackSimple.txt")

                            map_selected = 2
                            map1, map2, map3, leave = drawMapsMenu(
                                map_selected)

                        elif leave.collidepoint(pygame.mouse.get_pos()):
                            game_menu = 'main_menu'
                        else:
                            pass
                        g = Graph()
                        g.createGraphCartesian(mapa)

                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_ESCAPE:
                    #         game_menu = 'main_menu'

                elif game_menu == "algoritmos":

                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if a_estrela.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[0].alg_selected = 0

                        elif greedybf.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[0].alg_selected = 1
                            

                        elif greedy.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[0].alg_selected = 2
                            

                        elif bfs.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[0].alg_selected = 3
                            

                        elif dfs.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[0].alg_selected = 4
                            

                        elif a_estrela2.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[1].alg_selected = 0

                        elif greedybf2.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[1].alg_selected = 1
                            

                        elif greedy2.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[1].alg_selected = 2
                           

                        elif bfs2.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[1].alg_selected = 3
                            

                        elif dfs2.collidepoint(pygame.mouse.get_pos()):

                            jogo.players[1].alg_selected = 4
                            

                        elif leave_alg.collidepoint(pygame.mouse.get_pos()):
                            game_menu = 'main_menu'
                        else:
                            pass
                    a_estrela, greedybf, greedy, bfs, dfs, a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg = drawAlgoritmosMenu(
                        alg_selected,jogo.players)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'
                elif game_menu == "players":

                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if one.collidepoint(pygame.mouse.get_pos()):

                            jogo.resetPlayers(mapa)

                            jogo.n_players = 1
                            players_selected = 0
                            
                            one, two, leave = drawJogMenu(
                                players_selected)
                        elif two.collidepoint(pygame.mouse.get_pos()):

                            jogo.resetPlayers(mapa)

                            jogo.n_players = 2
                            players_selected = 1
                            
                            one, two, leave = drawJogMenu(
                                players_selected)
                        elif leave.collidepoint(pygame.mouse.get_pos()):
                            game_menu = 'main_menu'
                        else:
                            pass

                elif game_menu == "pista":

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'

                elif game_menu == "main_menu":
                    jogo.resetPlayers(mapa)
                    # event mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "pista"
                            screen.fill((50, 50, 50))
                            drawMap(screen, mapa, jogo.getPlayers())
                            drawText("ESC to return", pygame.font.SysFont(
                                "arielblack", 40), COLOR_WHITE, 0, 0)

                        if maps.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "maps"
                            screen.fill((50, 50, 50))

                            map1, map2, map3, leave = drawMapsMenu(
                                map_selected)

                        if algoritmos.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "algoritmos"
                            screen.fill((50, 50, 50))

                            a_estrela, greedybf, greedy, bfs, dfs, a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg = drawAlgoritmosMenu(
                        alg_selected,jogo.players)

                        if players.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "players"
                            screen.fill((50, 50, 50))

                            one, two, leave = drawJogMenu(
                                players_selected)

                        if quit_game.collidepoint(pygame.mouse.get_pos()):
                            running = False

                    # if event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_ESCAPE:
                    #         game_menu = 'main_menu'

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


def main():

    jogo = Jogo("tracks/trackCircle.txt")

    jogo.startPYGame()


if __name__ == "__main__":
    main()

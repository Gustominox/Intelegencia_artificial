
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

    def __init__(self, trackFile):
        self.players = []
        self.mapa = Mapa(trackFile)
        self.fps = 10

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
                                          in self.mapa.finish],g)
            
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

            path.append((novaPosicao.x,novaPosicao.y))
            res.getPltXY(path)
            self.mapa.show()
            res.showPath(path,True)

            time.sleep(1)

    def startPYGame(self):
        running = True

        mapa = Mapa("tracks/track.txt")
        jogador = Player(Vector(1,3))
        game_menu = "main_menu"


        while running:

            # Background colour
            screen.fill((50, 50, 50))

            #CHECK MENU

            if game_menu == "maps":
                pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/3) -10, (monitor_size.current_h/5) - 2, 105    , 30 ))
                drawText("Mapa1", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/3, monitor_size.current_h/5)


            if game_menu == 'main_menu':
                start = pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/2.5) -10, (monitor_size.current_h/4) - 2, 210    , 30 ))
                drawText("1.Choose Map", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/2.5, monitor_size.current_h/4)

                quit_game = pygame.draw.rect(screen, (0,0,0), pygame.Rect((monitor_size.current_w/2.5) -10, (monitor_size.current_h/4) + 50, 210    , 30 ))
                drawText("Quit", pygame.font.SysFont("arielblack", 40), (255,255,255), monitor_size.current_w/2.5, monitor_size.current_h/4 + 50)

            elif game_menu == 'pista':
                
                jogo = Jogo("tracks/track.txt")

                # jogo.start()

                drawMap(screen,mapa)
                player(jogador)
                drawText("ESC to return", pygame.font.SysFont("arielblack", 40), (255,255,255), 0, 0)

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_menu = 'main_menu'
                        if event.key == pygame.K_1:
                            game_menu = 'pista'

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start.collidepoint(pygame.mouse.get_pos()):
                            game_menu = "pista"
                        if quit_game.collidepoint(pygame.mouse.get_pos()):
                            running = False


                    if event.type == pygame.QUIT:
                        running = False 

            pygame.display.update()




def main():

    jogo = Jogo("tracks/track.txt")

    jogo.startPYGame()

    # print(jogo.proximasJogadas(jogador))

    # print(res.greedyJog(jogador.estado, jogo.proximasJogadas(jogador), [Vector(9,3)]))


if __name__ == "__main__":
    main()

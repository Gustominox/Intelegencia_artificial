
from player import Player
from mapa import *
from vector import Vector
from resolver import Resolver
from grafo import Graph
import time


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

            #jog = res.greedyJog(jogador, [Vector(x, y) for x, y
            #                              in self.mapa.finish])

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


def main():

    jogo = Jogo("tracks/track.txt")

    jogo.start()

    # print(jogo.proximasJogadas(jogador))

    # print(res.greedyJog(jogador.estado, jogo.proximasJogadas(jogador), [Vector(9,3)]))


if __name__ == "__main__":
    main()

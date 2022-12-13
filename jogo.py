
from player import Player
from mapa import Mapa
from vector import Vector

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

    def proximasJogadas(self, player):

        proximasJogadas = []

        for jogada in JOGADAS:
            proximasJogadas.append(player.velocidade + jogada)

        return proximasJogadas


def main():
    
    jogo = Jogo("track.txt")
    jogador = Player()
    print(jogo.proximasJogadas(jogador))

if __name__ == "__main__":
    main()

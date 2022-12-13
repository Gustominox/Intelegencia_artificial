
from player import Player
from mapa import Mapa
from vector import Vector
from resolver import Resolver

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
            proximasJogadas.append(player.estado + player.velocidade + jogada)

        return proximasJogadas


def main():
    
    res = Resolver()
    
    
    jogo = Jogo("track.txt")
    jogador = Player()
    jogador.estado = Vector(0,0)
    # jogador.aumentaVelocidade(Vector(1,1))
    
    print(jogo.proximasJogadas(jogador))

    print(res.greedyJog(jogador.estado, jogo.proximasJogadas(jogador), [Vector(9,3)]))

if __name__ == "__main__":
    main()


from player import Player
from mapa import Mapa
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

        proximasJogadas = []

        for jogada in JOGADAS:
            proximasJogadas.append(player.estado + player.velocidade + jogada)

        return proximasJogadas

    def addPlayer(self, player):
        self.players.append(player)

    def draw(self):
        print(self.players[0])
        print(self.mapa)

    

    def start(self):
        
        res = Resolver()
        jogador = Player(estadoInicial=Vector(0,0))
        
        self.addPlayer(jogador)
        
        on = 1 * self.fps
        g = Graph()
    
        g.createGraphCartesian(self.mapa)
        while on:
            time.sleep(1 / self.fps)
            
            jog = res.greedyJog(jogador.estado, self.proximasJogadas(jogador), [Vector(x,y) for x,y 
                                                                                in self.mapa.finish])
            
            g.checkPath(jogador.estado,jog)
            
            jogador.jogada(jog)
            self.draw()
            
            on -= 1
    
        
            
        
            

def main():
    
    
    
    jogo = Jogo("tracks/track.txt")
    
    
    jogo.start()
    
    # print(jogo.proximasJogadas(jogador))

    # print(res.greedyJog(jogador.estado, jogo.proximasJogadas(jogador), [Vector(9,3)]))

if __name__ == "__main__":
    main()

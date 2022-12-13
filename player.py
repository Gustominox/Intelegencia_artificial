
from vector import Vector

class Player:
    
    def __init__(self,estadoInicial):
        self.estado = estadoInicial
        self.velocidade = Vector(0,0)        
    
    def __str__(self):
        return f"Player: Estado -> {self.estado}\tVelocidade -> {self.velocidade}"
        
    def aumentaVelocidade(self,vector):
        self.velocidade += vector
    
    def jogada(self,jogada):
        self.aumentaVelocidade(jogada)
        self.estado += self.velocidade
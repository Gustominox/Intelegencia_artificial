
from vector import Vector

class Player:
    
    def __init__(self):
        self.estado = (None,None)
        self.velocidade = Vector(0,0)        
        
    def aumentaVelocidade(self,vector):
        self.velocidade += vector
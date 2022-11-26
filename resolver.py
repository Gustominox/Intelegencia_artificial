from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import Mapa
from grafo import Graph
class Resolver:
    def __init__(self,trackFile):
        self.path = []
        self.mapa = Mapa(trackFile)
    def __str__(self):
        # string = "[ \n"
        # for line in self.content:
        #     string = string + str(line) + "," + "\n"
        # string = string + "]"
        # return string
        return self
    
    def getPltXY(self):
        # self.path = [(1.0, 3.0), (2.0, 3.0), (3.0, 4.0), (4.0, 4.0), (5.0, 4.0), (6.0, 4.0), (7.0, 4.0), (8.0, 4.0), (9.0, 4.0)]
        xpath = [x + 0.5 for (x,y) in self.path]
        ypath = [y + 0.5 for (x,y) in self.path]
        return (xpath,ypath)
    
    def setMap(self,mapa):
        self.mapa = mapa
    
    def showPath(self,final=False):
        self.mapa.show()
        x,y = self.getPltXY()
        plt.plot(x,y,'b.--', linewidth=2, markersize=20)
        
        if final:
            plt.show()
    
    def createGraph(self):
        (xstart,ystart) = self.mapa.start
        self.path = []
        grafo = Graph()
        # print(f"LINES:{self.mapa.lines} ROWS:{self.mapa.rows}")
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1): # nao quero procurar na propria celula
                    search = (i-1+xstart,j-1+ystart)
                    
                    if self.mapa.getCelValue(search) == 1:
                        grafo.addNode(f"{search}",0)
                        self.path.append(search)
        # for node in self.path:
            # for addNode in self.path:
                # if addNode != node:
                    # grafo.addEdge(node, addNode, 10)
        grafo.desenha()
        return

def main():
        
    resolver = Resolver("track.txt")
    print(resolver.mapa)
    print(resolver.mapa.finish)
    resolver.createGraph()
    resolver.showPath()
    
    plt.show()

    
    
if __name__ == "__main__":
    main()
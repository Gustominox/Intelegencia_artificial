from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import *
from grafo import Graph




class Resolver:
    def __init__(self, trackFile):
        self.path = []
        self.mapa = Mapa(trackFile)
        self.grafo = Graph()

    def __str__(self):
        # string = "[ \n"
        # for line in self.content:
        #     string = string + str(line) + "," + "\n"
        # string = string + "]"
        # return string
        return self

    def getPltXY(self,path):
        xpath = [x + 0.5 for (x, y) in path]
        ypath = [y + 0.5 for (x, y) in path]
        return (xpath, ypath)

    def setMap(self, mapa):
        self.mapa = mapa

    def showPath(self,path, final=False):
        x, y = self.getPltXY(path)
        plt.plot(x, y, 'b.--', linewidth=2, markersize=20)

        if final:
            plt.show()

    def createGraph(self):
        (xstart, ystart) = self.mapa.start

        # debug
        self.path = []
        ###
        self.mapa.show()
        
        self.grafo.addNode(f"{self.mapa.start}", 0)
        self.addEdges(xstart, ystart,[])
        # print(f"LINES:{self.mapa.lines} ROWS:{self.mapa.rows}")
        
        # for node in nextNodes:

        
        return

    def addEdges(self,xstart,ystart,visited,depth=0):
        nextNodes = []
        depth += 1
        if (depth == 10): return
        visited.append((xstart,ystart))
        # print(f"VISITED: {visited}")
        # plt.show()
        
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):  # nao quero procurar na propria celula
                    search = (i-1+xstart, j-1+ystart)
                    # if i == 2 and j == 1:
                    if search not in visited:
                        if self.mapa.getCelValue(search) == TRACK:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(str((xstart, ystart)), str(search), 10)
                            nextNodes.append(search)
                            # self.grafo.desenha()
                            
                            # debug
                            ###
                        elif self.mapa.getCelValue(search) == FINISH:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(str((xstart, ystart)), str(search), 10)
                            
                            visited.append(search)
                            self.path.append( visited)
                            return
                            
                            
                            
                            
        for (x,y) in nextNodes:
            # self.showPath(True)4
            # self.mapa.show()
            # plt.plot([xstart+0.5,x+0.5],[ystart+0.5,y+0.5] , 'b.--', linewidth=2, markersize=20)
            
            self.addEdges(x, y,visited.copy(),depth)
            
            
            
                    

def main():
    
    resolver = Resolver("track.txt")
    print(resolver.mapa)
    print(resolver.mapa.finish)
    resolver.createGraph()
    plt.show()
    resolver.grafo.desenha()
    # print(resolver.mapa.getCelValue((9,3)))
    
    print(resolver.path.__len__())
    for path in resolver.path:
        resolver.mapa.show()   
        resolver.showPath(path)
        plt.show()



if __name__ == "__main__":
    main()

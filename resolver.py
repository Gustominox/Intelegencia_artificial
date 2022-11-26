from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import Mapa
class Resolver:
    def __init__(self):
        self.path = []
        self.mapa = Mapa()
    def __str__(self):
        # string = "[ \n"
        # for line in self.content:
        #     string = string + str(line) + "," + "\n"
        # string = string + "]"
        # return string
        return self
    
    def getPltXY(self):
        self.path = [(1.0, 3.0), (2.0, 3.0), (3.0, 4.0), (4.0, 4.0), (5.0, 4.0), (6.0, 4.0), (7.0, 4.0), (8.0, 4.0), (9.0, 4.0)]
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
            

def main():
        
    resolver = Resolver()
    mapa = Mapa()
    mapa.read_file("track.txt")
    print(mapa)
    mapa.initStartFinish()
    resolver.setMap(mapa)

    resolver.showPath()
    plt.show()

    
    
if __name__ == "__main__":
    main()
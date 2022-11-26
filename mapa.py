from matplotlib import pyplot as plt
from matplotlib import colors

class Mapa:

    def __init__(self):
        self.content = []
        self.start = (-1,-1)
        self.finish = []
        self.rows = -1
        self.lines = -1
        

    def __str__(self):
        string = "[ \n"
        for line in self.content:
            string = string + str(line) + "," + "\n"
        string = string + "]"
        return string

    def read_file(self, filename):

        fich = open(filename, "r")
        text = fich.read()

        matriz = []
        line = []
        x = 0
        y = 0
        for char in text:
            if char == 'X':
                line.append(0)
                # line.append('X')
            if char == '-':
                line.append(1)
                # line.append('-')
            if char == 'F':
                line.append(2)
                # line.append('F')
            if char == 'P':
                line.append(3)
                # line.append('P')
            if char == '\n':
                y += 1
                x = 0
                matriz.append(line)
                line = []
            x += 1
        matriz.append(line) 
        self.rows = x-1
        self.lines = y +1 
        
        
        self.content = matriz
        
    def initStartFinish(self):
        x = 0 
        y = 0
        for line in self.content:
            if 3 in line:
                for elem in line:
                    print(elem)
                    if elem == 3:
                        self.start = (x,self.lines-y)
                        break
                    x += 1
                break
            y += 1
        print (self.start)
        return        

    def show(self,final=False):
        cmap = colors.ListedColormap(['Black', 'white','red','green'])
        plt.figure(figsize=(10, 10))
        plt.pcolor(self.content[::-1], cmap=cmap)# edgecolors='k', linewidths=3)

        if final: 
            plt.show()
    
def main():
    mapa = Mapa()
    mapa.read_file("track.txt")
    print(mapa)
    mapa.initStartFinish()

    resolver = Resolver()

    cmap = colors.ListedColormap(['Black', 'white','red','green'])
    plt.figure(figsize=(10, 10))
    plt.pcolor(mapa.content[::-1], cmap=cmap)# edgecolors='k', linewidths=3)
    x,y = resolver.getPltXY()
    plt.plot(x,y,'b.--', linewidth=2, markersize=12)
    
    plt.show()
    

if __name__ == "__main__":
    main()

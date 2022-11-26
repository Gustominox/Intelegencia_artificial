from matplotlib import pyplot as plt
from matplotlib import colors
from resolver import Resolver

class Mapa:

    def __init__(self):
        self.content = []

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
                matriz.append(line)
                line = []
        matriz.append(line)        
        self.content = matriz


def main():
    mapa = Mapa()
    mapa.read_file("track.txt")
    print(mapa)

    resolver = Resolver()

    cmap = colors.ListedColormap(['Black', 'white','red','green'])
    plt.figure(figsize=(10, 10))
    plt.pcolor(mapa.content[::-1], cmap=cmap)# edgecolors='k', linewidths=3)
    x,y = resolver.getPltXY()
    plt.plot(x,y,'b.--', linewidth=2, markersize=12)
    
    plt.show()
    

if __name__ == "__main__":
    main()

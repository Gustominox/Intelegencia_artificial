from matplotlib import pyplot as plt
from matplotlib import colors


class Matriz:

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
    matriz = Matriz()
    matriz.read_file("track.txt")
    print(matriz)


    cmap = colors.ListedColormap(['Black', 'white','red','green'])
    plt.figure(figsize=(10, 10))
    plt.pcolor(matriz.content[::-1], cmap=cmap)# edgecolors='k', linewidths=3)
    xpath = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    x = [val - 0.5 for val in xpath]
    ypath = [3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    y = [val + 0.5 for val in ypath]
    print(y)
    plt.plot(x,y,'b.--', linewidth=2, markersize=12)
    # plt.plot(2.5,3.5,'b|--', linewidth=2, markersize=12)
    # plt.plot(3.5,4.5,'b_--', linewidth=2, markersize=12)

    plt.show()
    

if __name__ == "__main__":
    main()

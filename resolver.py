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
            # debug
            # self.showPath(True)4
            # self.mapa.show()
            # plt.plot([xstart+0.5,x+0.5],[ystart+0.5,y+0.5] , 'b.--', linewidth=2, markersize=20)
            
            self.addEdges(x, y,visited.copy(),depth)
        
        def procura_DFS(self, start, end, path=[], visited=set()):
            path.append(start)
            visited.add(start)

            if start == end:
                # calcular o custo do caminho funçao calcula custo.
                custoT = self.calcula_custo(path)
                return (path, custoT)
            for (adjacente, peso) in self.m_graph[start]:
                if adjacente not in visited:
                    resultado = self.procura_DFS(adjacente, end, path, visited)
                    if resultado is not None:
                        return resultado
            path.pop()  # se nao encontra remover o que está no caminho......
            return None

            
            
                    

def main():
    
    resolver = Resolver("track.txt")
    print(resolver.mapa)
    print(resolver.mapa.start)
    print(resolver.mapa.finish)
    resolver.createGraph()
    plt.show()
    resolver.grafo.desenha()
    
    # print(resolver.path.__len__())
    # for path in resolver.path:
    #     resolver.mapa.show()   
    #     resolver.showPath(path)
    #     plt.show()
        
    g = resolver.grafo
        
    #cosntrução de menu
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-DFS")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            #Escrever o grafo como string
            print(g)
            l=input("prima enter para continuar")
        elif saida == 2:
            #Desenhar o grafo de forma gráfica
            g.desenha()
        elif saida == 3:
            #Imprimir as chaves do dicionario que representa o grafo
            print(g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            #imprimir todas as arestas do grafo
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            #Efetuar  pesquisa de caminho entre nodo inicial e final com DFS
            inicio=input("Nodo inicial->")
            fim = input("Nodo final->")
            
            inicio = "(1, 3)"
            fim = "(9, 3)"
            (path, custoT) = g.procura_DFS( inicio, fim, path=[], visited=set())
            p = [tuple(map(int, nodo.replace('(', '').replace(')', '').split(', '))) for nodo in path]
            print (f"{p}, custo: {custoT}")
            resolver.mapa.show()   
            resolver.showPath(p)
            
            plt.show()
            resolver.grafo.desenha()
            plt.show()
                    
            l = input("prima enter para continuar")
        elif saida == 6:
            #Efetuar  pesquisa de caminho entre nodo inicial e final com DFS
            inicio=input("Nodo inicial->")
            fim = input("Nodo final->")
            print(g.procura_BFS(  fim, queue=[inicio],visited=[],path=[]))
            l = input("prima enter para continuar")
        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")
            





if __name__ == "__main__":
    main()

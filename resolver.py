from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import *
from grafo import Graph




class Resolver:
    def __init__(self, trackFile):
        self.path = []
        self.mapa = Mapa(trackFile)
        self.grafo = Graph()
    
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

        self.path = []
        self.grafo.addNode(f"{self.mapa.start}", 0)
        self.addEdges(xstart, ystart,[])
        

        
        return

    def addEdges(self,xstart,ystart,visited,depth=0):
        nextNodes = []
        depth += 1
        if (depth == 10): return
        visited.append((xstart,ystart))
        
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):  # nao quero procurar na propria celula
                    search = (i-1+xstart, j-1+ystart)
                    if search not in visited:
                        if self.mapa.getCelValue(search) == TRACK:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(str((xstart, ystart)), str(search), 10)
                            nextNodes.append(search)
                            
                        elif self.mapa.getCelValue(search) == FINISH:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(str((xstart, ystart)), str(search), 10)
                            
                            visited.append(search)
                            self.path.append( visited)
                            
                            
                            
                            
                            
        for (x,y) in nextNodes:
            self.addEdges(x, y,visited.copy(),depth)
        

            
            
                    

def main():
    
    resolver = Resolver("track.txt")
    ### Debug
    # print(resolver.mapa)
    # print(resolver.mapa.start)
    # print(resolver.mapa.finish)
    
    resolver.createGraph()
    
    
    
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
        print("3-Desenhar Mapa")
        print("4-Imprimir nodos de Grafo")
        print("5-Imprimir arestas de Grafo")
        print("6-DFS do Start ao Finish")
        print("7-DFS com selecao de Nodos")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            #Escrever o grafo como string
            print(g)
            l=input("prima enter para continuar")
        elif saida == 2:
            g.desenha()
            l=input("prima enter para continuar")
        elif saida == 3:
            #Desenhar o grafo de forma gráfica
            resolver.mapa.show(True)
            l=input("prima enter para continuar")
            
        elif saida == 4:
            #Imprimir as chaves do dicionario que representa o grafo
            print(g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 5:
            #imprimir todas as arestas do grafo
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 6:
            
            #Efetuar pesquisa de caminho entre nodo Start e Finish's com DFS
            
            inicio = "(1, 3)"
            fim = ["(9, 4)", "(9, 3)", "(9, 2)"]
            
            (path, custoT) = g.procura_DFS( inicio, fim, path=[], visited=set())
            p = [tuple(map(int, nodo.replace('(', '').replace(')', '').split(', '))) for nodo in path]
           
            # print (f"{p}, custo: {custoT}")
           
            resolver.mapa.show()   
            resolver.showPath(p)
            
            plt.show()
                    
            l = input("prima enter para continuar")
        elif saida == 7:
            #Efetuar  pesquisa de caminho entre nodo inicial e final com DFS
            inicio = input("Nodo inicial->")
            fim = [input("Nodo final->")]
            
            (path, custoT) = g.procura_DFS( inicio, fim, path=[], visited=set())
            p = [tuple(map(int, nodo.replace('(', '').replace(')', '').split(', '))) for nodo in path]
            # print (f"{p}, custo: {custoT}")
            resolver.mapa.show()   
            resolver.showPath(p)
            
            plt.show()
            resolver.grafo.desenha()
            plt.show()
                    
            l = input("prima enter para continuar")
        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")
            





if __name__ == "__main__":
    main()

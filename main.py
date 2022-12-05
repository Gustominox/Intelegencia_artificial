#Importar classes nodo e grafo
from grafo import Graph
from nodo import Node
from resolver import Resolver
from matplotlib import pyplot as plt
from matplotlib import colors

def main():

    
    resolver = Resolver("track.txt")

    resolver.createGraph()
    
    g = resolver.grafo
        
    #construção de menu
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Desenhar Mapa")
        print("4-Imprimir nodos de Grafo")
        print("5-Imprimir arestas de Grafo")
        print("6-DFS do Start ao Finish")
        print("7-DFS com selecao de Nodos")
        print("8-BFS do Start ao Finish")
        print("0-Sair")

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
        elif saida == 8:
            
            #Efetuar pesquisa de caminho entre nodo Start e Finish's com BFS
            
            inicio = "(1, 3)"
            fim = ["(9, 4)", "(9, 3)", "(9, 2)"]
            
            (path, custo) = g.bfs(inicio, fim)
            p = [tuple(map(int, nodo.replace('(', '').replace(')', '').split(', '))) for nodo in path]
           
            # print (f"{p}, custo: {custoT}")
           
            resolver.mapa.show()   
            resolver.showPath(p)
            
            plt.show()
                    
            l = input("prima enter para continuar")    
        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()

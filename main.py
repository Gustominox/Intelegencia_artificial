#Importar classes nodo e grafo
from grafo import Graph
from nodo import Node
from mapa import Mapa
from resolver import Resolver
from matplotlib import pyplot as plt
from matplotlib import colors
from vector import Vector
from jogo import Jogo

def main():

    resolver = Resolver()

    g = Graph()
    mapa = Mapa("tracks/track.txt")
    g.createGraphCartesian(mapa)
        
    #construção de menu
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Desenhar Mapa")
        print("4-Imprimir nodos de Grafo")
        print("5-Imprimir arestas de Grafo")
        print("6-Start Game")
        print("7-DFS do Start ao Finish")
        print("8-BFS do Start ao Finish")
        print("9-GreedySearch do Start ao Finish")
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
            mapa.show(True)
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
            #imprimir todas as arestas do grafo
            
            jogo = Jogo()

            jogo.startPYGame()
            
            l = input("prima enter para continuar")
        elif saida == 7:
            
            #Efetuar pesquisa de caminho entre nodo Start e Finish's com DFS
            
            inicio = Vector(1, 3)
            fim = [Vector(9, 4), Vector(9, 3), Vector(9, 2)]
            
            (path, custoT) = resolver.dfs( inicio, fim,g, path=[], visited=set())
            p = [(vector.x,vector.y)for vector in path]
           
            # print (f"{p}, custo: {custoT}")
           
            mapa.show()   
            resolver.showPath(p)
            
            plt.show()
                    
            l = input("prima enter para continuar")
       
        elif saida == 8:
            
            #Efetuar pesquisa de caminho entre nodo Start e Finish's com BFS
            
            
            (path, custo) = resolver.bfs(inicio, fim,g)
            p = [(vector.x,vector.y)for vector in path]
           
           
            mapa.show()   
            resolver.showPath(p)
            
            plt.show()
                    
            l = input("prima enter para continuar")
        elif saida == 9:
            
            #Efetuar pesquisa de caminho entre nodo Start e Finish's com DFS
            
            inicio = Vector(1, 3)
            fim = [Vector(9, 4), Vector(9, 3), Vector(9, 2)]
           
            (path, custoT) = resolver.greedy_search(inicio, fim,g, path=[])
            p = [(vector.x,vector.y)for vector in path]
           
            # print (f"{p}, custo: {custoT}")
           
            mapa.show()   
            resolver.showPath(p)
            
            plt.show()
                    
            l = input("prima enter para continuar")        
        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()

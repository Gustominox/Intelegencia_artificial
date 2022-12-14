# LICENCIATURA EM ENGENHARIA INFORMÁTICA
# MESTRADO integrado EM ENGENHARIA INFORMÁTICA

# Inteligência Artificial
# 2022/23

# Draft Ficha 1


# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import networkx as nx
# Biblioteca de tratamento de grafos necessária para desenhar graficamente o grafo
import matplotlib.pyplot as plt

# biblioteca necessária para se poder utilizar o valor math.inf  (infinito)
import math

# Importar a classe nodo
from nodo import Node
from mapa import *
from vector import Vector

# Definição da classe grafo:
# Um grafo tem uma lista de nodos,
# um dicionário:  nome_nodo -> lista de tuplos (nome_nodo,peso)
# para representar as arestas
# uma flag para indicar se é direcionado ou não


class Graph:
    # Construtor da classe
    def __init__(self, directed=False):
        self.m_nodes = []   # lista de nodos do grafo
        self.m_directed = directed   # se o grafo é direcionado ou nao
        self.m_graph = {}  # dicionario para armazenar os nodos, arestas  e pesos

        self.debug = []

    ##############################
    # Escrever o grafo como string
    ##############################

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + \
                str(self.m_graph[key]) + "\n"
        return out

    #####################################
    # Adicionar aresta no grafo, com peso
    ####################################

    def addNode(self, node1, estimativa):
        # cria um objeto node  com o nome passado como parametro
        n1 = Node(node1, estimativa)

        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[node1] = set()
        return n1

    def addEdge(self, node1, node2, weight):  # node1 e node2 são os 'nomes' de cada nodo
        if not node2 in self.m_graph[node1]:
            self.m_graph[node1].add((node2, weight))

        # se o grafo for nao direcionado, colocar a aresta inversa
        if not self.m_directed:
            self.m_graph[node2].add((node1, weight))

    ################################
    # Encontrar nodo pelo nome
    ################################
    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None


    def get_node_by_vector(self, vector):
        
        name = str((vector.x,vector.y))
        print(name)
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None



    ###########################
    # Imprimir arestas
    ###########################

    def imprime_aresta(self):
        listaA = ""
        for nodo in self.m_graph.keys():
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + \
                    nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################################
    # Devolver o custo de uma aresta
    ################################
    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]    # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    ######################################
    # Dado um caminho calcula o seu custo
    #####################################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nomes de nodos
        teste = caminho
        custo = 0
        i = 0
        while i+1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i+1])
            i = i+1
        return custo

    ###########################
    # desenha grafo  modo grafico
    #########################
    def desenha(self):
        # criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()

        # Converter para o formato usado pela biblioteca networkx
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        # desenhar o grafo
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    def dist(self, x0, y0, x1, y1):
        a = (x1 - x0)**2 + (y1 - y0)**2
        b = math.sqrt(a)
        return b

    def distnodos(self, node1, node2):
        tuplo1 = node1.nodetotuple()
        tuplo2 = node2.nodetotuple()
        r = self.dist(tuplo1[0], tuplo1[1], tuplo2[0], tuplo2[1])
        return r

    def createGraphCartesian(self, mapa):
        self.addNode(f"{(0, 0)}", 0)

        for line in range(mapa.lines):
            for row in range(mapa.rows):
                print((row, line))
                for i in range(3):
                    for j in range(3):
                        # nao quero procurar na propria celula
                        if not ((i == 1 and j == 1) or
                                (i == 0 and j == 0) or
                                (i == 0 and j == 2) or
                                (i == 2 and j == 0) or
                                (i == 2 and j == 2)):

                            x = i-1+row
                            y = j-1+line
                            search = (x, y)

                            if x > -1 and x < mapa.rows and y > -1 and y < mapa.lines:

                                print(f"adding {search}")

                                # self.addNode(str(search), 0)
                                # self.addEdge(str((row, line)),
                                #              str(search), 1)

                                if mapa.getCelValue(search) == TRACK:
                                    self.addNode(str(search), TRACK)
                                    self.addEdge(str((row, line)),
                                                 str(search), 1)

                                if mapa.getCelValue(search) == WALL:
                                    self.addNode(str(search), WALL)
                                    self.addEdge(str((row, line)),
                                                 str(search), 25)

                                if mapa.getCelValue(search) == START:
                                    self.addNode(str(search), START)
                                    self.addEdge(str((row, line)),
                                                 str(search), 1)

                                elif mapa.getCelValue(search) == FINISH:
                                    self.addNode(str(search), FINISH)
                                    self.addEdge(str((row, line)),
                                                 str(search), 1)
    # deprecated

    def createGraph1(self, mapa):
        (xstart, ystart) = mapa.start
        self.addNode(f"{mapa.start}", 0)
        self.addEdges(xstart, ystart, mapa)

    # deprecated
    def addEdges(self, xstart, ystart, mapa, visited=[], depth=0):

        nextNodes = []
        depth += 1
        # if (depth == 10):
        #     return
        visited.append((xstart, ystart))

        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):  # nao quero procurar na propria celula
                    search = (i-1+xstart, j-1+ystart)

                    if search not in visited:
                        if mapa.getCelValue(search) == TRACK:
                            self.addNode(str(search), 0)
                            self.addEdge(str((xstart, ystart)), str(search), 1)
                            nextNodes.append(search)

                        if mapa.getCelValue(search) == WALL:
                            self.addNode(str(search), 0)
                            self.addEdge(str((xstart, ystart)),
                                         str(search), 25)

                        elif mapa.getCelValue(search) == FINISH:
                            self.addNode(str(search), 0)
                            self.addEdge(str((xstart, ystart)), str(search), 1)

        for (x, y) in nextNodes:
            self.addEdges(x, y, mapa, visited, depth)  # visited.copy(), depth)

    def checkPath(self, inicio, destino):
        custo = destino-inicio
        print(f"{inicio} -> {destino}")
        x = custo.x
        y = custo.y
        currentPosition = inicio
        
        while x != 0 or y != 0:
            lastPosition = currentPosition
            
            nodeType = self.get_node_by_vector(currentPosition).type
            
            if  nodeType == FINISH:
                print("FINISH")
                return currentPosition, FINISH
            if  nodeType == WALL:
                print("WALL")
                return lastPosition, WALL
            
            
            
            
            if x > 0:
                x = x-1
                currentPosition += Vector(1,0)
            elif x < 0:
                x = x+1
                currentPosition += Vector(-1,0)
                
                
            if y > 0:
                y = y-1
                currentPosition += Vector(0,1)
            elif y < 0:
                y = y+1
                currentPosition += Vector(0,-1)
            
            nodeType = self.get_node_by_vector(currentPosition).type
            
            if  nodeType == FINISH:
                print("FINISH")
                return currentPosition, FINISH
            if  nodeType == WALL:
                print("WALL")
                return lastPosition, WALL
            
            print(f"CURRENT POSITION :{currentPosition} NODETYPE :{nodeType}")

        return currentPosition, TRACK
    
        print(f"{currentPosition} == {destino}")


def main():
    mapa = Mapa("trackCircle.txt")
    g = Graph()
    g.createGraphCartesian(mapa)
    g.desenha()


if __name__ == "__main__":
    main()

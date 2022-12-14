from matplotlib import pyplot as plt
from matplotlib import colors
from grafo import Graph
from queue import PriorityQueue
from mapa import *


JOGADAS = [
    Vector(-1, -1),
    Vector(-1, 0),
    Vector(0, -1),
    Vector(0, 0),
    Vector(0, 1),
    Vector(1, 0),
    Vector(1, 1),
    Vector(-1, 1),
    Vector(1, -1),
]


class Resolver:
    def __init__(self):
        self.path = []

    def getPltXY(self, path):
        xpath = [x + 0.5 for (x, y) in path]
        ypath = [y + 0.5 for (x, y) in path]
        return (xpath, ypath)

    def showPath(self, path, final=False):
        x, y = self.getPltXY(path)
        plt.plot(x, y, 'b.--', linewidth=2, markersize=20)

        if final:
            plt.show()

    ################################################################################
    # Procura DFS
    ####################################################################################

    def dfs(self, start, end, grafo, path=[], visited=set()):

        path.append(start)
        visited.add(start)

        if start in end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = grafo.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in grafo.m_graph[start]:
            if adjacente not in visited:
                resultado = self.dfs(adjacente, end, grafo, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    ################################################
    # Procura BFS
    ################################################

    def bfs(self, start, end, grafo):
        queue = [[start]]
        visited = set()

        while queue:
            # print(visited)
            # Gets the first path in the queue
            path = queue.pop(0)
            # print(f"PATH: {path}")

            # Gets the last node in the path
            vertex = path[-1]
            grafo.debug.append(vertex)
            # print(f"VERTEX: {vertex}")

            # Checks if we got to the end
            if vertex in end:
                custoT = grafo.calcula_custo(path)
                return (path, custoT)
                # return (grafo.debug, custoT)
            # We check if the current node is already in the visited nodes set in order not to recheck it
            elif vertex not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for (current_neighbour, peso) in grafo.m_graph[vertex]:
                    if current_neighbour not in visited:
                        new_path = list(path)
                        new_path.append(current_neighbour)
                        queue.append(new_path)

                # Mark the vertex as visited
                visited.add(vertex)

    ################################
    # Greedy search
    ################################

    def greedy_search(self, start, end, grafo, path=[]):
        path.append(start)
        max = (1000, start)
        if start in end:
            custoT = grafo.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in grafo.m_graph[start]:
            if adjacente not in path:
                for node in end:
                    dist = grafo.distnodos(grafo.get_node_by_name(
                        adjacente), grafo.get_node_by_name(node))
                    if dist < max[0]:
                        max = (dist, adjacente)
        self.greedy_search(max[1], end, grafo, path)
        return (path, 0)

    ##################################
    # A* search
    ##################################

    def a_estrela_search(self, start, end, grafo):
        q = PriorityQueue()
        q.put((0, [start]))
        visited = set()

        while q:
            # Gets the first path in the queue
            nextItem = q.get()
            print(nextItem)
            path = nextItem[1]

            # Gets the last node in the path
            node = path[-1]

            # Checks if we got to the end
            if grafo.get_node_by_vector(node).type == FINISH:
                custoT = grafo.calcula_custo(path)
                return (path, custoT)
                # return (grafo.debug, custoT)
            # We check if the current node is already in the visited nodes set in order not to recheck it
            elif node not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for (current_neighbour, peso) in grafo.m_graph[node]:
                    if current_neighbour not in visited:
                        if grafo.get_node_by_vector(current_neighbour).type != WALL:
                            dist = 1000
                            for meta in end:
                                dtemp = current_neighbour.distance_to(meta)
                                if dtemp < dist:
                                    dist = dtemp
                            new_path = list(path)
                            new_path.append(current_neighbour)
                            q.put(dist + grafo.calcula_custo(new_path), new_path)

                # Mark the node as visited
                visited.add(node)

    ##################################
    # Greedy search jogada
    ##################################
    
    def greedyJog(self,player, end):
        estado = player.estado

        max = (1000, estado)
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            for node in end:
                dist = candidato.distance_to(node)
                if dist < max[0]:
                    max = (dist, jogada)
        return max[1]

    ######################################
    # A* jogada
    ######################################

    def aestrelaJog(self, player, end, grafo):
        estado = player.estado
        mincusto = (1000, estado)
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            (path, custo) = self.a_estrela_search(candidato, end, grafo)
            if custo < mincusto:
                mincusto = (custo, jogada)
        return mincusto[1]

    def main():
        return

    if __name__ == "__main__":
        main()

from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import *
from grafo import Graph


class Resolver:
    def __init__(self, trackFile):
        self.path = []
        self.mapa = Mapa(trackFile)
        self.grafo = Graph()

    def getPltXY(self, path):
        xpath = [x + 0.5 for (x, y) in path]
        ypath = [y + 0.5 for (x, y) in path]
        return (xpath, ypath)

    def setMap(self, mapa):
        self.mapa = mapa

    def showPath(self, path, final=False):
        x, y = self.getPltXY(path)
        plt.plot(x, y, 'b.--', linewidth=2, markersize=20)

        if final:
            plt.show()

    def createGraph(self):
        (xstart, ystart) = self.mapa.start

        self.path = []
        self.grafo.addNode(f"{self.mapa.start}", 0)
        self.addEdges(xstart, ystart)

        return

    def addEdges(self, xstart, ystart, visited=[], depth=0):
        nextNodes = []
        depth += 1
        if (depth == 10):
            return
        visited.append((xstart, ystart))

        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):  # nao quero procurar na propria celula
                    search = (i-1+xstart, j-1+ystart)
                    if search not in visited:
                        if self.mapa.getCelValue(search) == TRACK:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(
                                str((xstart, ystart)), str(search), 1)
                            nextNodes.append(search)

                        elif self.mapa.getCelValue(search) == FINISH:
                            self.grafo.addNode(f"{search}", 0)
                            self.grafo.addEdge(
                                str((xstart, ystart)), str(search), 1)

        for (x, y) in nextNodes:
            self.addEdges(x, y, visited.copy(), depth)

    ################################################################################
    # Procura DFS
    ####################################################################################
    def dfs(self, start, end, grafo, path=[], visited=set(),):

        path.append(start)
        visited.add(start)

        if start in end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = grafo.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in grafo.m_graph[start]:
            if adjacente not in visited:
                resultado = grafo.procura_DFS(adjacente, end, path, visited)
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
                    a = grafo.distnodos(grafo.get_node_by_name(adjacente), grafo.get_node_by_name(node))
                    if a < max[0]:
                        max = (a, adjacente)
        grafo.greedy_search(max[1], end, path)


def main():
    return


if __name__ == "__main__":
    main()

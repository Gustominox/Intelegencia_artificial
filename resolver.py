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
        """Retorna o caminho PLT

        Args:
            path (List): Lista com nodos do caminho

        Returns:
            Tuple: Tuplo de uma Lista de todos os x's e outra de todos os y's para serem desenhados
        """        
        xpath = [x + 0.5 for (x, y) in path]
        ypath = [y + 0.5 for (x, y) in path]
        return (xpath, ypath)

    def showPath(self, path, final=False):
        """Mostra o caminho PLT

        Args:
            path (List): Lista com todos os nodos do caminho
            final (bool, optional): Quando é TRUE, demonstra o mapa. Quando é FALSE, guarda em cache e 
            mostra mais tarde com o plt.show()
        """        
        x, y = self.getPltXY(path)
        plt.plot(x, y, 'b.--', linewidth=2, markersize=20)

        if final:
            plt.show()

    ################################################################################
    # Procura DFS
    ####################################################################################

    def dfs(self, start, end, grafo, path=[], visited=set()):
        """Algortimo de Procura "Depth First Search"

        Args:
            start (Vector): Vector (Ponto) onde começa a Procura
            end (List): Objetivo de Procura
            grafo (Graph): Grafo onde é feita a Procura 
            path (List, Vector): Lista de Vectores (Pontos). 
            visited (List, Vector): Lista dos Vectores (pontos) já visitados.

        Returns:
            None
        """        

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
        """Algortimo de Procura "Breadth First Search"

        Args:
            start (Vector): Vector (Ponto) onde começa a procura
            end (List): Objetivo de Procura
            grafo (Graph): Grafo onde é feita a Procura
        """        
        # Inicialização da queue
        queue = [[start]]
        visited = set()

        while queue:
            # Retira-se o próximo caminho da queue
            path = queue.pop(0)

            # Obtém-se o últmio nodo do caminho em questão
            node = path[-1]

            # Verifica-se se atingimos uma das casas de chegada
            if node in end:
                custoT = grafo.calcula_custo(path)
                return (path, custoT)
            # Verifica-se se o nodo em questão não havia sido visitado anteriormente
            elif node not in visited:
                # Enumeram-se todos os adjacentes do nodo em análise, colocando todos os possíveis caminhos na queue
                for (current_neighbour, peso) in grafo.m_graph[node]:
                    if current_neighbour not in visited:
                        new_path = list(path)
                        new_path.append(current_neighbour)
                        queue.append(new_path)

                # Marca-se o nodo analisado como visitado
                visited.add(node)

    ################################
    # Greedy search
    ################################

    def greedy_search(self, start, end, grafo, path=[]):

        """Algortimo Guloso de Procura

        Returns:
            List: Lista de Vectores (Pontos) de objetivo à Procura
        """        
        # Perante o nodo em análise, é sempre escolhido o adjacente com melhor distância estimada à meta
        path.append(start)
        max = (1000, start)
        if start in end:
            custoT = grafo.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in grafo.m_graph[start]:
            if adjacente not in path:
                for node in end:
                    dist = adjacente.distance_to(node)
                    if dist < max[0]:
                        max = (dist, adjacente)
        # De seguida, repete-se o processo no adjacente escolhido até eventualmente chegar à meta                
        self.greedy_search(max[1], end, grafo, path)
        return (path, 0)

    ####################################
    # Greedy Best-First Search
    ####################################
    
    def greedy_bf_search(self, start, end, grafo):
        
        # Inicialização da Priority Queue
        q = PriorityQueue()
        q.put((0, [start]))
        visited = set()

        while not q.empty():
            # Retira-se o caminho com maior prioridade da queue
            nextItem = q.get()
            path = nextItem[1]

            # Obtém-se o últmio nodo do caminho em questão
            node = path[-1]

            # Verifica-se se atingimos uma das casas de chegada
            if grafo.get_node_by_vector(node).type == FINISH:
                custoT = grafo.calcula_custo(path)
                return (path, custoT)
            # Verifica-se se o nodo em questão não havia sido visitado anteriormente
            elif node not in visited:
                # Enumeram-se todos os adjacentes do nodo em análise, colocando todos os possíveis caminhos na queue
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
                            # O caminho é adicionado na queue com prioridade igual à sua distância estimada à meta
                            q.put((dist, new_path))

                # Marca-se o nodo analisado como visitado
                visited.add(node)
    
    ##################################
    # A* search
    ##################################

    def a_estrela_search(self, start, end, grafo):
        # Inicialização da Priority Queue
        q = PriorityQueue()
        q.put((0, [start]))
        visited = set()

        while not q.empty():
            # Retira-se o caminho com maior prioridade da queue
            nextItem = q.get()
            path = nextItem[1]

            # Obtém-se o últmio nodo do caminho em questão
            node = path[-1]

            # Verifica-se se atingimos uma das casas de chegada
            if grafo.get_node_by_vector(node).type == FINISH:
                custoT = grafo.calcula_custo(path)
                return (path, custoT)
            # Verifica-se se o nodo em questão não havia sido visitado anteriormente
            elif node not in visited:
                # Enumeram-se todos os adjacentes do nodo em análise, colocando todos os possíveis caminhos na queue
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
                            # O caminho é adicionado na queue com prioridade igual à soma da sua distância estimada à meta com o custo do caminho até então
                            q.put((dist + grafo.calcula_custo(new_path), new_path))

                # Marca-se o nodo analisado como visitado
                visited.add(node)

    ##################################
    # Greedy search jogada
    ##################################
    def proximasJogadas(self, player):
        """Jogadas seguintes no Algortimo Guloso de Procura

        Args:
            player (Player): Jogador a efetuar as Jogadas

        Returns:
            List: Lista com  todas as possíveis proximas coordenadas a partir do estado e velocidade do jogador
            """

        proximasJogadas = []

        for jogada in JOGADAS:
            proximasJogadas.append(player.estado + player.velocidade + jogada)

        return proximasJogadas

    def greedyJog(self,player, end):

        """Apenas uma Jogada Greedy

        Returns:
            Tuple: Tuplo onde está inserida a melhor
        """        
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
    # DFS Jogada
    ######################################
    
    def dfsJog(self, player, end, grafo):
        estado = player.estado
        mincusto = (1000, estado)
        counter_validos = 0
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            if grafo.vector_exists(candidato):
                nodo = grafo.get_node_by_vector(candidato)
                nodoType = nodo.type
                if nodoType != WALL:
                    counter_validos = counter_validos + 1
                    (path, custo) = self.dfs(candidato, end, grafo, path=[], visited=set())
                    if custo < mincusto[0]:
                        mincusto = (custo, jogada)
        if counter_validos != 0:                
            return mincusto[1]
        return JOGADAS[3]
    
    ######################################
    # BFS Jogada
    ######################################
    
    def bfsJog(self, player, end, grafo):
        estado = player.estado
        mincusto = (1000, estado)
        counter_validos = 0
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            if grafo.vector_exists(candidato):
                nodo = grafo.get_node_by_vector(candidato)
                nodoType = nodo.type
                if nodoType != WALL:
                    counter_validos = counter_validos + 1
                    (path, custo) = self.bfs(candidato, end, grafo)
                    if custo < mincusto[0]:
                        mincusto = (custo, jogada)
        if counter_validos != 0:                
            return mincusto[1]
        return JOGADAS[3]
    
    
    ######################################
    # Greedy Best-First Jogada
    ######################################
    
    def gbfJog(self, player, end, grafo):
        estado = player.estado
        mincusto = (1000, estado)
        counter_validos = 0
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            if grafo.vector_exists(candidato):
                nodo = grafo.get_node_by_vector(candidato)
                nodoType = nodo.type
                if nodoType != WALL:
                    counter_validos = counter_validos + 1
                    (path, custo) = self.greedy_bf_search(candidato, end, grafo)
                    if custo < mincusto[0]:
                        mincusto = (custo, jogada)
        if counter_validos != 0:                
            return mincusto[1]
        return JOGADAS[3]
    
    ######################################
    # A* jogada
    ######################################

    def aestrelaJog(self, player, end, grafo):
        estado = player.estado
        mincusto = (1000, estado)
        counter_validos = 0
        print("Calculando caminho...")
        for jogada in JOGADAS:
            candidato = player.estado + player.velocidade + jogada
            if grafo.vector_exists(candidato):
                nodo = grafo.get_node_by_vector(candidato)
                nodoType = nodo.type
                if nodoType != WALL:
                    counter_validos = counter_validos + 1
                    (path, custo) = self.a_estrela_search(candidato, end, grafo)
                    if custo < mincusto[0]:
                        mincusto = (custo, jogada)
        print("Caminho calculado :)")
        if counter_validos != 0:                
            return mincusto[1]
        return JOGADAS[3]

    def main():
        return

    if __name__ == "__main__":
        main()

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # inicializar fila para a bfs e um set de nos por direções visitadas
        num_nodes = len(graph)
        q_BFS = deque([(1<<i,i,0) for i in range(num_nodes)])
        visited_paths = set((1<<i,i) for i in range(num_nodes))

        # mascara que contém todos os bits como 1 para mostrar que todos os nos 
        # foram atingidos
        finished_mask = (1 << num_nodes) - 1

        # bfs
        while(q_BFS):
            mask,node,steps = q_BFS.popleft()
            
            # se atingir a mascara meta
            if mask == finished_mask:
                return steps
            
            # visita os nos não visitados e adiciona 1 ao caminho
            for adj in graph[node]:
                new_mask = mask | (1 << adj)
                if (new_mask,adj) not in visited_paths:
                    visited_paths.add((new_mask,adj))
                    q_BFS.append((new_mask,adj,steps+1))

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Mapeia nós originais para suas cópias correspondentes
        node_map = {}
        
        # Inicia a cópia com o nó original
        copy = Node(node.val)
        node_map[node] = copy
        
        # Fila para percorrer os nós do grafo original
        queue = deque([node])
        
        while queue:
            current_node = queue.popleft()
            
            # Para cada vizinho do nó atual
            for neighbor in current_node.neighbors:
                # Se o vizinho ainda não foi visitado
                if neighbor not in node_map:
                    # Cria uma cópia do vizinho e adiciona à fila
                    node_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Adiciona a cópia do vizinho à lista de vizinhos da cópia do nó atual
                node_map[current_node].neighbors.append(node_map[neighbor])
        
        return copy

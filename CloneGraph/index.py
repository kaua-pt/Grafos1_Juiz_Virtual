from collections import deque

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
        
        node_map = {}
        
        copy = Node(node.val)
        node_map[node] = copy
        
        queue = deque([node])
        
        while queue:
            current_node = queue.popleft()
            
            for neighbor in current_node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                node_map[current_node].neighbors.append(node_map[neighbor])
        
        return copy

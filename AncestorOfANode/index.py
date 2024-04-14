class Solution(object):
    def getAncestors(self, n, edges):
        ancestors_list = []

        graph = {}
        for edge in edges:
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        def dfs(node, visited, ancestors):
            visited[node] = True
            if node in graph:
                for adjacent_node in graph[node]:
                    if not visited[adjacent_node]:
                        ancestors.append(adjacent_node)
                        dfs(adjacent_node, visited, ancestors)

        for node in range(n):
            visited = [False] * n
            aux_list = []
            dfs(node, visited, aux_list)
            aux_list.sort()
            ancestors_list.append(aux_list)

        return ancestors_list

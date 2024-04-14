class Solution(object):
    def getAncestors(self, n, edges):
        ancestors_list = []

        def dfs(node, visited, ancestors):
            visited[node] = True
            for edge in edges:
                if node == edge[1] and not visited[edge[0]]:
                    ancestors.append(edge[0])
                    dfs(edge[0], visited, ancestors)

        for node in range(n):
            visited = [False] * n
            aux_list = []
            dfs(node, visited, aux_list)
            aux_list.sort()
            ancestors_list.append(aux_list)

        return ancestors_list
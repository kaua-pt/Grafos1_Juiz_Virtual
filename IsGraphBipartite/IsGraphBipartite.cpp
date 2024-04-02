#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    bool bfs(vector<vector<int>> &graph, vector<int> &color, int i)
    {
        queue<int> q;
        q.push(i);
        while (!q.empty())
        {
            int u = q.front();
            q.pop();
            for (int v : graph[u])
            {
                if (color[v] == -1)
                {
                    q.push(v);
                    color[v] = 1 - color[u];
                }
                else if (color[v] == color[u])
                {
                    return false;
                }
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>> &graph)
    {
        int n = graph.size();
        vector<int> color(n, -1);

        for (int i = 0; i < n; i++)
        {
            if (color[i] == -1 && bfs(graph, color, i) == false)
                return false;
        }
        return true;
    }
};
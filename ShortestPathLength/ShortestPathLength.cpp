class Solution
{
public:
    int shortestPathLength(vector<vector<int>> &graph)
    {
        int n = graph.size();
        int max = (1 << n) - 1; // indicativo para ver se todos os nos foram lidos
        queue<pair<int, pair<int, int>>> q;
        set<pair<int, int>> visitados;

        for (int i = 0; i < n; i++)
        {
            q.push({i, {1 << i, 0}});
            visitados.insert({i, 1 << i});
        }

        // bfs
        while (!q.empty())
        {

            auto f = q.front();
            q.pop();

            // se a bfs tiver compreendido todos os nos
            if (f.second.first == max)
                return f.second.second;

            for (auto vizinho : graph[f.first])
            {
                int novaMascara = f.second.first || (1 << vizinho);
                if (visitados.find({vizinho, novaMascara}) != visitados.end())
                {
                    visitados.insert({vizinho, novaMascara});
                    q.push({vizinho, {novaMascara, f.second.second + 1}});
                }
            }
        }
        return -1;
    }
};
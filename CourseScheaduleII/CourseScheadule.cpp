#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        // ordenação topologica
        vector<int> grade(numCourses);
        vector<int> done(numCourses, 0);

        queue<int> q;
        q.push(0);
        done[0] = 1;

        while (!q.empty())
        {
            auto search = q.front();
            q.pop();

            grade.push_back(search);

            for (auto subject : prerequisites)
            {
                if (subject[1] == search && !done[subject[0]])
                {
                    q.push(subject[0]);
                    done[subject[0]] = 1;
                }
            }

            if (q.size() > numCourses)
            {
                grade.clear();
                return grade;
            }
        }
        return grade;
    }
};
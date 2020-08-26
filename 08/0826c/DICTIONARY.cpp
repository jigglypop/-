#include <iostream>
#include <cstring>
#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

void printer(const vector<vector<int>> &graph)
{
    for (int y = 0; y < graph.size(); ++y)
    {
        for (int x = 0; x < graph[y].size(); ++x)
        {
            cout << graph[y][x] << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> graph;

void makeGraph(const vector<string> &words)
{
    graph = vector<vector<int>>(26, vector<int>(26, 0));
    for (int j = 1; j < words.size(); ++j)
    {
        int i = j - 1, len = min(words[i].size(), words[j].size());
        for (int k = 0; k < len; ++k)
        {
            if (words[i][k] != words[j][k])
            {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';

                graph[a][b] = 1;
                break;
            }
        }
    }
}

vector<int> visited, order;

void dfs(int current)
{
    visited[current] = 1;

    for (int next = 0; next < graph.size(); ++next)
        if (graph[current][next] && !visited[next])
            dfs(next);
    order.push_back(current);
}

vector<int> topologicalSort()
{
    int m = graph.size();
    visited = vector<int>(m, 0);
    order.clear();

    for (int i = 0; i < m; ++i)
        if (!visited[i])
            dfs(i);

    reverse(order.begin(), order.end());

    // 역방향 간선이 있는 경우 --> DAG가 아님
    for (int i = 0; i < m; ++i)
        for (int j = i + 1; j < m; ++j)
            if (graph[order[j]][order[i]])
                return vector<int>();

    return order;
}

int main()
{
    freopen("DICTIONARY.txt", "r", stdin);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<string> words(n);
        for (auto &w : words)
        {
            cin >> w;
        }
        makeGraph(words);
        // auto orders = topologicalSort();
        // if (orders.empty())
        // {
        //     cout << "INVALID HYPOTHESIS\n";
        // }
        // else
        // {
        //     for (auto &o : orders)
        //         cout << static_cast<char>(o + 'a');
        //     cout << '\n';
        // }
    }

    return 0;
}
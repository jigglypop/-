#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int main()
{
    freopen("11279.txt", "r", stdin);
    priority_queue<int> pq;
    int N, n;
    for (scanf("%d", &N); N--;)
    {
        scanf("%d", &n);
        if (n)
            pq.push(n);
        else
        {
            printf("%d\n", pq.empty() ? 0 : pq.top());
            if (!pq.empty())
            {
                pq.pop();
            }
        }
    }
    return 0;
}
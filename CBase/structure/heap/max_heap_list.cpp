#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int heap[100001];
int last;
int pop()
{
    int ans = heap[1];
    heap[1] = heap[last];
    heap[last--] = 0;
    for (int i = 1; i * 2 <= last;)
    {
        if (heap[i] > heap[i * 2] && heap[i] > heap[i * 2 + 1])
        {
            break;
        }
        else if (heap[i * 2] > heap[i * 2 + 1])
        {
            swap(heap[i], heap[i * 2]);
            i = i * 2;
        }
        else
        {
            swap(heap[i], heap[i * 2 + 1]);
            i = i * 2 + 1;
        }
    }
    return ans;
}
void push(int x)
{
    heap[++last] = x;
    for (int i = last; i > 1; i /= 2)
    {
        if (heap[i / 2] < heap[i])
        {
            swap(heap[i / 2], heap[i]);
        }
        else
        {
            break;
        }
    }
}

void Print()
{
    for (auto i : heap)
    {
        if (i != 0)
        {
            printf("%d ", i);
        }
    }
}
int main()
{
    freopen("heap.txt", "r", stdin);
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int x;
        scanf("%d", &x);
        if (x == 0)
        {
            if (last == 0)
            {
                printf("0\n");
            }
            else
            {
                printf("%d\n", pop());
            }
        }
        else
        {
            push(x);
        }
    }

    return 0;
}
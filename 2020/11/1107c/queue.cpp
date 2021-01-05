#include <iostream>
#include <cstring>
#include <string>
using namespace std;

struct Stack
{
    int data[10000];
};

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("queue.txt", "r", stdin);
    int N;
    cin >> N;
    // for (int i = 0; i < N; i++)
    // {
    //     string cmd;
    //     cin >> cmd;
    //     if (cmd == "push")
    //     {
    //         int num;
    //         cin >> num;
    //         s.push(num);
    //     }
    //     else if (cmd == "top")
    //     {
    //         cout << (s.empty() ? -1 : s.top()) << '\n';
    //     }
    //     else if (cmd == "size")
    //     {
    //         cout << s.size << '\n';
    //     }
    //     else if (cmd == "empty")
    //     {
    //         cout << s.empty() << '\n';
    //     }
    //     else if (cmd == "pop")
    //     {
    //         cout << (s.empty() ? -1 : s.top()) << '\n';
    //         if (!s.empty())
    //         {
    //             s.pop();
    //         }
    //     }
    // }
    return 0;
}
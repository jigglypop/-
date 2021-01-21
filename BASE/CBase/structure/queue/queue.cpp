#include <iostream>
#include <cstring>
#include <string>
using namespace std;

struct Queue
{
    int data[10000];
    int begin, end;
    Queue()
    {
        begin = 0;
        end = 0;
    }
    void push(int num)
    {
        data[end] = num;
        end += 1;
    }
    bool empty()
    {
        if (begin == end){
            return true;
        }
        else{
            return false;
        }
    }
    int size()
    {
        return end - begin;
    }
    int front()
    {
        return data[begin];
    }
    int back()
    {
        return data[end-1];
    }
    int pop(){
        if (empty()){
            return -1;
        }else{
            begin += 1;
            return data[begin];
        }

    }
};

int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("queue.txt", "r", stdin);
    int N;
    cin >> N;
    Queue Q;
    for (int i = 0; i < N; i++)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "push")
        {
            int num;
            cin >> num;
            Q.push(num);
        }
        else if (cmd == "pop")
        {
            if (Q.empty())
            {
                cout << -1 << '\n';
            }
            else
            {
                cout << Q.front() << '\n';
                Q.pop();
            }
        }
        else if (cmd == "size")
        {
            cout << Q.size() << '\n';
        }
        else if (cmd == "empty")
        {
            cout << Q.empty() << '\n';
        }
        else if (cmd == "front")
        {
            if (Q.empty())
            {
                cout << -1 << '\n';
            }
            else
            {
                cout << Q.front() << '\n';
            }
        }
        else if (cmd == "back")
        {
            if (Q.empty())
            {
                cout << -1 << '\n';
            }
            else
            {
                cout << Q.back() << '\n';
            }
        }
    }
    return 0;
}
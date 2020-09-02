#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

const int INF = 987654321;
int cache[10000];
string num;

int classify(int start, int end)
{
    string part = num.substr(start, end - start + 1);
    if (part == string(part.size(), part[0]))
    {
        return 1;
    }
    bool progressive = true;
    for (int i = 0; i < part.size() - 1; i++)
    {
        if (part[i + 1] - part[i] != part[1] - part[0])
        {
            progressive = false;
        }
    }

    if (progressive && abs(part[1] - part[0]) == 1)
    {
        return 2;
    }
    bool alternate = true;
    for (int i = 0; i < part.size(); i++)
    {
        if (part[i] != part[i % 2])
        {
            alternate = false;
        }
    }

    if (alternate)
    {
        return 4;
    }
    if (progressive)
    {
        return 5;
    }
    return 10;
}

int memorize(int idx)
{
    if (idx == num.size())
    {
        return 0;
    }
    int &ret = cache[idx];
    if (ret != -1)
    {
        return ret;
    }
    ret = INF;
    for (int i = 3; i <= 5; i++)
    {
        if (idx + i <= num.size())
        {
            ret = min(ret, memorize(idx + i) + classify(idx, idx + i - 1));
            cout << "ret : " << ret << endl;
        }
    }
    return ret;
}

int main(void)
{
    freopen("PI.txt", "r", stdin);
    int N;
    cin >> N;
    if (N < 1 || N > 50)
        exit(-1);
    for (int i = 0; i < N; i++)
    {
        memset(cache, -1, sizeof(cache));
        cin >> num;
        cout << memorize(0) << endl;
    }
    return 0;
}

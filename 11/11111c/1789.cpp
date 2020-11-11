#include <iostream>
#include <cstring>

using namespace std;
int main()
{
    freopen("1789.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long n;
    long long sum = 0;
    long long count = 1;
    cin >> n;
    while (1)
    {
        sum += count;
        if (sum > n)
        {
            --count;
            break;
        }
        ++count;
    }
    cout << count << endl;

    return 0;
}
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

struct Lecture
{
    int p, d;
};
bool cmp(const Lecture &u, const Lecture &v)
{
    return u.d > v.d;
}

using namespace std;
int main()
{
    freopen("2109.txt", "r", stdin);
    int n;
    cin >> n;
    vector<Lecture> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i].p >> A[i].d;
    }
    sort(A.begin(), A.end(), cmp);
    int k = 0;
    priority_queue<int> q;
    int ans = 0;
    for (int i = 10000; i >= 1; i--)
    {
        while (k < n && A[k].d == i)
        {
            q.push(A[k].p);
            k += 1;
        }
        if (!q.empty())
        {
            ans += q.top();
            q.pop();
        }
    }
    cout << ans << '\n';
    return 0;
}
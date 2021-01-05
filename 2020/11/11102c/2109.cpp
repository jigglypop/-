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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    vector<Lecture> A(n);
    for (int i = 0; i < n; i++)
        cin >> A[i].p >> A[i].d;
    sort(A.begin(), A.end(), cmp);
    int k = 0;
    priority_queue<int> Q;
    int ans = 0;
    for (int i = 10000; i >= 1; i--)
    {
        while (k < n && A[k].d == i)
        {
            Q.push(A[k].p);
            k += 1;
        }
        if (!Q.empty())
        {
            ans += Q.top();
            Q.pop();
        }
    }
    cout << ans << '\n';
    return 0;
}
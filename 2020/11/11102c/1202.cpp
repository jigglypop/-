#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>
#include <set>
using namespace std;
struct jewel
{
    int a, b;
};
int main()
{
    freopen("1202.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, K;
    cin >> N >> K;
    vector<jewel> A(N);
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        A[i].a = a;
        A[i].b = b;
    }
    sort(A.begin(), A.end(), [](jewel a, jewel b) {
        return a.b > b.b;
    });
    for (auto a : A)
    {
        cout << a.a << " " << a.b << "\n";
    };
    multiset<int> s;
    for (int i = 0; i < K; i++)
    {
        int t;
        cin >> t;
        s.insert(t);
    }
    long long ans = 0;
    for (int i = 0; i < N; i++)
    {
        auto it = s.lower_bound(A[i].a);
        if (it != s.end())
        {
            ans += A[i].b;
            s.erase(it);
        }
    }
    cout << ans << "\n";
    return 0;
}
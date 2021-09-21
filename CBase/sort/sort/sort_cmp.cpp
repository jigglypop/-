#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point
{
    int x, y;
};
bool cmp(const Point &u, const Point &v)
{
    if (u.x < v.x)
        return true;
    else if (u.x == v.x)
        return u.y < v.y;
    else
        return false;
}
int main()
{
    freopen("sort_pair.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    cin >> N;
    vector<Point> A(N);
    for (int i = 0; i < N; i++)
        cin >> A[i].x >> A[i].y;
    sort(A.begin(), A.end(), cmp);
    for (int i = 0; i < A.size(); i++)
        cout << A[i].x << " " << A[i].y << "\n";
    return 0;
}
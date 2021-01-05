#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int C, N, longest;
int x[101], y[101], radius[101];
struct Tree
{
    vector<Tree *> children;
};

// 성벽 a가 성벽 b를 포함하는지 확인
bool enclose(int a, int b)
{
    if (radius[a] > radius[b])
    {
        int dx = x[a] - x[b], dy = y[a] - y[b];
        // 두 성벽(원)의 중점간 거리의 제곱
        double diffOfRadius = pow(dx, 2) + pow(dy, 2);
        // 두 성벽의 반지름 차이의 제곱
        double distOfCenter = pow(radius[a] - radius[b], 2);
        if (diffOfRadius < distOfCenter)
            return true;
    }
    return false;
}

bool isChild(int parent, int child)
{
    if (!enclose(parent, child))
        return false;
    // 두 성벽사이에 다른 성벽이 있는지 확인
    // 즉, 직계 부모-자식 관계인지 확인
    for (int i = 0; i < N; i++)
    {
        // 부모도 자식도 아닌 성벽(노드, 원)이 부모 노드에 포함되면서, child를 포함하는지 확인
        if (i != parent && i != child && enclose(parent, i) && enclose(i, child))
            return false;
    }
    return true;
}

//root 성벽을 루트로 하는 트리를 생성
Tree *getTree(int root)
{
    Tree *tmp = new Tree();
    for (int i = 0; i < N; i++)
    {
        if (isChild(root, i))
        {
            // ch 성벽이 root 성벽에 직접적으로 포함되어 있다면
            // 트리를 만들고 자손 목록에 추가한다
            tmp->children.push_back(getTree(i));
        }
    }
    return tmp;
}

int height(Tree *root)
{
    vector<int> heights;
    for (int i = 0; i < root->children.size(); i++)
        heights.push_back(height(root->children[i]));
    if (heights.empty())
        return 0;
    // 각 서브트리별 높이를 정렬
    sort(heights.begin(), heights.end());
    // 서브트리 개수가 2개 이상인지 확인
    if (heights.size() >= 2)
        // 오름차순 정렬 했으므로, 가장 큰 높이 2개 추출
        longest = max(longest, 2 + heights[heights.size() - 2] + heights[heights.size() - 1]);
    // 만약 서브트리가 1개 였다면 트리의 높이+1에 해당
    return heights.back() + 1;
}

int solve(Tree *root)
{
    longest = 0;
    int h = height(root);
    return max(longest, h);
}

int main()
{
    freopen("fortress.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> C;
    while (C--)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
        {
            cin >> x[i] >> y[i] >> radius[i];
        }
        Tree *T = getTree(0);
        cout << solve(T) << endl;
    }
    return 0;
}

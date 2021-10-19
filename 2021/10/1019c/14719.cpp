#include <iostream>
#include <vector>
using namespace std;

int main()
{
    freopen("14719.txt", "r", stdin);
    int H, W, result;
    cin >> H >> W;
    vector<int> board(W);
    vector<int> left(W);
    vector<int> right(W);
    for (int i = 0; i < W;i++) {
        int temp;
        cin >> temp;
        left[i] = temp;
        right[i] = temp;
        board[i] = temp;
    }
    for (int i = 1; i < W;i++) {
        left[i] = max(left[i], left[i - 1]);
    }
    for (int i = W - 2; i >= 0;i--) {
        right[i] = max(right[i], right[i + 1]);
    }
    result = 0;
    for (int i = 0; i < W;i++) {
        result += min(right[i], left[i]) - board[i];
    }
    printf("%d", result);
    return 0;
}
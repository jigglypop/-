#include <stdio.h>
#include <algorithm>

using namespace std;
int A[100002];
int main() {
    freopen("11441.txt", "r", stdin);
    int N, M;
    scanf("%d", &N);
    for (int i = 0; i < N;i++){
        int tmp;
        scanf("%d ", &tmp);
        if (i > 0) {
            A[i + 1] += A[i] + tmp;
        } else {
            A[i + 1] = tmp;
        }
    }
    scanf("%d", &M);
    for (int i = 0; i < M;i++){
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", A[b] - A[a - 1]);
    }
    return 0;
}
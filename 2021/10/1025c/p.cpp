#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void print(int **pp) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << pp[i][j] << " ";
        }
        cout << endl;
    }
}

int main(void) {
    int arr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int *temp[3];
    for (int i = 0; i < 3;i++) {
        int *p = arr[i];
        temp[i] = p;
    }
    int **pp = temp;
    print(pp);
}
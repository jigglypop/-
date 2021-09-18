#include <stdio.h>

void print(int *ptr, int n) {
    for (int i = 0; i < n;i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");
}

void swap(int *arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
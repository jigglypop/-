#include <stdio.h>
#include <stdlib.h>
#include "util.h"

void bubble_sort(int *arr, int N) 
{
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N - 1; j++) {
            if (arr[j] > arr[j + 1])
                swap(arr, j, j + 1);
        }
    }
}

int main()
{
    int arr[10] = { 8, 4, 2, 5, 3, 7, 10, 1, 6, 9 };
    int N = sizeof(arr) / sizeof(int);
    bubble_sort(arr, N);  
    print(arr, N);
    return 0;
}
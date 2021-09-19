#include <stdio.h>

void print(char (*board)[251], int Y, int X) {
    for (int y = 0; y < Y;y++) {
        for (int x = 0; x < X;x++) {
            printf("%c ", board[y][x]);
        }
    }
}
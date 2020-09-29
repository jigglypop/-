#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int i = 5, j = 4, k = 1, l, m;
    l = i > 5 || j != 0;
    m = j <= 4 && k < 1;
    printf("%d, %d\n", l, m);
    return 0;
}
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int hap, j, k, l;
    j = k = l = 0;
    hap = ++j + k++ + ++l;
    printf("%d, %d, %d, %d\n", hap, j, k, l);
    return 0;
}
#include <iostream>
#include <cstring>
using namespace std;

struct Point
{
    int xpos;
    int ypos;
};

int main()
{
    Point pos1 = {1, 2};
    Point pos2 = {3, 4};
    Point *ptr = &pos2;
    printf("%d %d", ptr->xpos, ptr->ypos);
    return 0;
}
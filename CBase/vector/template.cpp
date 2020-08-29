#include <iostream>
#include <string>

using namespace std;

template <typename T>
T sum(T a, T b)
{
    return a + b;
}

int main()
{
    cout << sum<int>(3, 4) << endl;
    return 0;
}
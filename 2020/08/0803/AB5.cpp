#include <iostream>

using namespace std;

int main()
{
    int A, B;
    while (1)
    {
        cin >> A >> B;
        if (A != 0 || B != 0)
        {
            cout << A + B
                 << "\n";
        }
        else
        {
            break;
        }
    }
}
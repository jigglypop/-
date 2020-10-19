#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<int, int> m;
    m[5] = 100;
    m[3] = 30;
    map<int, int>::iterator iter;
    for (iter = m.begin(); iter != m.end(); ++iter)
    {
        cout << "(" << iter->first << ", " << iter->second << ")"
             << " ";
    }
    cout << endl;

    m[5] = 200;

    for (iter = m.begin(); iter != m.end(); ++iter)
    {
        cout << "(" << iter->first << ", " << iter->second << ")"
             << " ";
    }
    cout << endl;
}
#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> s;
    for (int i = 0; i < 10; i++)
    {
        s.insert(i);
    }
    set<int>::iterator iter;
    for (iter = s.begin(); iter != s.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;
    s.insert(9);
    s.insert(9);
    for (iter = s.begin(); iter != s.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;
    return 0;
}
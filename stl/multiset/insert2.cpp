#include <iostream>
#include <set>
using namespace std;

int main()
{
    multiset<int> ms;
    ms.insert(50);
    ms.insert(30);
    ms.insert(80);
    ms.insert(80);
    ms.insert(30);
    ms.insert(70);
    ms.insert(10);

    multiset<int>::iterator iter;

    for (iter = ms.begin(); iter != ms.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;

    cout << "30 : " << ms.count(30) << endl;
    iter = ms.find(30);
    cout << "iter : " << *iter << endl;

    return 0;
}
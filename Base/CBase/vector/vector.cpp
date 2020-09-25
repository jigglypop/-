#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    const auto new_end(remove(begin(v), end(v), 2));
    v.erase(new_end, end(v));
    for (auto i : v)
    {
        cout << i << ", ";
    }
    cout << "\n";
    const auto odd([](int i) { return i % 2 != 0; });
    v.erase(remove_if(begin(v), end(v), odd), end(v));
    // v.shrink_to_fit();
    for (auto i : v)
    {
        cout << i << ", ";
    }
    cout << "\n";
    return 0;
}
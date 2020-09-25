#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <cassert>

using namespace std;

void insert_sorted(vector<string> &v, const string &word)
{
    const auto insert_pos(lower_bound(begin(v), end(v), word));
    v.insert(insert_pos, word);
}

int main()
{
    vector<string> v{"some", "random", "words", "without", "order", "aaa", "yyy"};
    assert(false == is_sorted(begin(v), end(v)));
    sort(begin(v), end(v));
    assert(true == is_sorted(begin(v), end(v)));
    insert_sorted(v, "foobar");
    insert_sorted(v, "zzz");
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << "\n";
    return 0;
}
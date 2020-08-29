#include <iostream>
#include <functional>
#include <list>
#include <map>

using namespace std;

struct billionaire
{
    string name;
    double dollars;
    string country;
};

int main()
{

    list<billionaire> billionaires{
        {"A", 1.1, "korea"},
        {"B", 1.1, "japan"},
        {"C", 1.1, "usa"},
    };
    map<string, pair<const billionaire, size_t>> m;
    for (const auto &b : billionaires)
    {
        auto [iterator, success] = m.try_emplace(b.country, b, 1);
    }
    return 0;
}
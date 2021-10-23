#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
using namespace std;

map<string, int> m;
int K = 0, L = 0;
vector<pair<string, int> > v;
 
bool cmp(const pair<string, int> & a, const pair<string, int> & b) {
    return a.second < b.second;
}
 
int main(void) {
    freopen("13414.txt", "r", stdin);
    string s;
    scanf("%d %d", &K, &L);
    for (int i = 1; i <= L; i++) {
        cin >> s;
        m[s] = i; 
    }
    auto itr = m.begin();
    while (itr != m.end()) {
        v.push_back({ itr->first, itr->second }); 
        ++itr;
    }
    sort(v.begin(), v.end(), cmp); 
    if (K <= v.size()) {
        for (int i = 0; i < K; i++) cout << v.at(i).first << '\n';
    }
    else {
        for (int i = 0; i < v.size(); i++) cout << v.at(i).first << '\n';
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Trie
{
    struct Node
    {
        int children[26];
        bool valid;
        Node()
        {
            for (int i = 0; i < 26; i++)
            {
                children[i] = -1;
            }
            valid = false;
        }
    };
    vector<Node> trie;
};

int main()
{
    freopen("14425.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    Trie trie;
    return 0;
}
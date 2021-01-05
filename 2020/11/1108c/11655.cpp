

#include <iostream>
#include <string>
using namespace std;
string rot13(string s)
{
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] >= 'a' && s[i] <= 'm')
        {
            s[i] = s[i] + 13;
        }
        else if (s[i] >= 'n' && s[i] <= 'z')
        {
            s[i] = s[i] - 13;
        }
        else if (s[i] >= 'A' && s[i] <= 'M')
        {
            s[i] = s[i] + 13;
        }
        else if (s[i] >= 'N' && s[i] <= 'Z')
        {
            s[i] = s[i] - 13;
        }
    }
    return s;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("11655.txt", "r", stdin);
    string s;
    getline(cin, s);
    cout << rot13(s) << '\n';
}
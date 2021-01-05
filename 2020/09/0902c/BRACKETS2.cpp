#include <iostream>
#include <stack>

using namespace std;

bool Match(const string formula)
{
    const string opening("({["), closing(")}]");

    stack<char> S;
    for (int i = 0; i < formula.size(); ++i)
    {
        if (opening.find(formula[i]) != -1)
            S.push(formula[i]);
        else
        {
            if (S.empty())
                return false;
            if (opening.find(S.top()) != closing.find(formula[i]))
                return false;
            S.pop();
        }
    }
    return S.empty();
}

int main()
{
    freopen("BRACKETS2.txt", "r", stdin);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string formula;
        cin >> formula;
        if (Match(formula))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
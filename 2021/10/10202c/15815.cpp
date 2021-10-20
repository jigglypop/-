#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

int main()
{
    freopen("15815.txt", "r", stdin);
 	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	stack<int> st;
	string s;
	cin >> s;
	for(int i=0; i<s.length(); i++)
	{
		if(s[i] >= '0' && s[i] <= '9')
		{
			st.push(s[i] - '0');
		}
		else
		{
			int a = st.top();
			st.pop();
			int b = st.top();
			st.pop();
			
			if(s[i] == '+')
			{
				st.push(a+b);
			}
			else if(s[i] == '-')
			{
				st.push(b-a);
			}
			else if(s[i] == '*')
			{
				st.push(a*b);
			}
			else if(s[i] == '/')
			{
				st.push(b/a);
			}
		}
	}
	cout << st.top();
	return 0;
}
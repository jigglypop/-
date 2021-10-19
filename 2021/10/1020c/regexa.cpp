#include <stdio.h>
#include <string>
#include <regex>
using namespace std;

int main()
{
	string s = "123 456 789";
	regex number("[0-9]+");
	sregex_iterator it(s.begin(), s.end(), number);
	sregex_iterator end;
	while(it != end) {
		smatch m = *it;
		printf("%s\n", m.str(0).c_str());
		++it;
	}
	return 0;
}
#include <stdio.h>
#include <string>
#include <regex>

using namespace std;

int main()
{
	string s = "123";
	regex number("[0-9]+");
    regex email("[a-z]+@[a-z].[a-z]");
    if(regex_match(s, number))
	{
		printf("number\n");
        printf("%c", regex_match(s, number));
    }
	else
	{
		printf("not number\n");
	}
	return 0;
}
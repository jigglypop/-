#include <iostream>
using namespace std;
int main()
{
    int num;
    int firstNum;
    int secondNum;
    int sumNum;
    int result = 0;
    int cnt = 0;
    cin >> num;
    if (num < 10)
        num *= 10;
    result = num;
    while (1)
    {
        firstNum = result / 10;
        secondNum = result % 10;
        sumNum = firstNum + secondNum;
        result = (secondNum * 10) + (sumNum % 10);
        cnt++;
        if (num == result)
            break;
    }
    cout << cnt;
}

#include <stdio.h>
#include <string.h>

void print1(int (*X)(const char *))
{
    X("print1");
};
void print2(int (*X[2])(const char *))
{
    X[0]("print2");
    printf("문자열 길이 : %d \n", X[1]("aa"));
};

int main(void)
{
    int (*myfunc[2])(const char *);

    // myfunc[0] = puts;
    // myfunc[1] = strlen;

    // print1(myfunc[0]);
    // print2(myfunc);
    char s1[] = "Hello"; // 문자열을 할당할 때 배열의 크기를 생략하는 방법
    printf("%s\n", s1);  // Hello: %s로 문자열 출력
    return 0;
}
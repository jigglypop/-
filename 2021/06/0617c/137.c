#include <stdio.h>

int main(void)
{
    FILE *file;
    file = fopen("./file.txt", "w+");
    if (file == NULL)
    {
        printf("파일이 없습니다.");
    }
    else
    {
        char word[] = "hello";
        printf("%s\n", word);
        fputc(*word, file);
        printf("파일이 생성되었습니다.");
        fclose(file);
    }
    return 0;
}
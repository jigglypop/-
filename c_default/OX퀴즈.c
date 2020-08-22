#include <stdio.h>
#include <string.h>
char OX[80];

int main()
{
    int N, score, sum;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        sum = 0;
        score = 1;
        scanf("%s", &OX);
        for (int j = 0; j < strlen(OX); j++)
        {
            if (OX[j] == 'O')
            {
                sum += score;
                score++;
            }
            if (OX[j] == 'X')
                score = 1;
        }
        printf("%d\n", sum);
    }
    return 0;
}
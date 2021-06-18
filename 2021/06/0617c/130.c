#include <stdio.h>

int main(void)
{
    char *animal[3];
    char **panimal;
    animal[0] = "호랑이";
    animal[1] = "사자";
    animal[2] = "토끼";
    panimal = animal;
    puts(animal[0]);
    puts(panimal[1]);
    puts(panimal[2]);
}
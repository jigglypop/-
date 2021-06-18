#include <stdio.h>
#include <string.h>

struct Address
{
    char name[30];
    char phone[20];
    char address[100];
};

void print(struct Address *pad)
{
    printf("%s %s %s\n", pad->name, pad->phone, pad->address);
}

int main(void)
{
    struct Address ad;
    struct Address *pad;
    pad = &ad;
    strcpy(pad->name, "염동환2");
    strcpy(pad->phone, "010-6289-3572");
    strcpy(pad->address, "주소2");
    print(&ad);
    return 0;
}

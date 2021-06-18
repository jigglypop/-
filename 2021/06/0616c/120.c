#include <stdio.h>
#include <string.h>

struct Address
{
    char name[30];
    char phone[20];
    char address[100];
};

int main(void)
{
    struct Address ad;
    struct Address *pad;
    pad = &ad;
    strcpy((*pad).name, "염동환");
    strcpy((*pad).phone, "010-6289-3571");
    strcpy((*pad).address, "주소");
    printf("%s %s %s\n", ad.name, ad.phone, ad.address);
    strcpy(pad->name, "염동환2");
    strcpy(pad->phone, "010-6289-3572");
    strcpy(pad->address, "주소2");
    printf("%s %s %s\n", ad.name, ad.phone, ad.address);
    strcpy(ad.name, "염동환3");
    strcpy(ad.phone, "010-6289-3573");
    strcpy(ad.address, "주소3");
    printf("%s %s %s\n", ad.name, ad.phone, ad.address);
    return 0;
}

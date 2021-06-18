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
    strcpy(ad.name, "염동환");
    strcpy(ad.phone, "010-6289-3571");
    strcpy(ad.address, "주소");
    printf("%s %s %s", ad.name, ad.phone, ad.address);
    return 0;
}

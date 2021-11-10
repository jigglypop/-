#include <stdio.h>
#include <limits.h>
#include <string.h>

#define num 1000001

int main(void) {
	
	char apb[num]; 
	
	int count[123] = {0,};
	
	int max = INT_MIN;
	
	int max_apb, div=0, len;
	
	scanf("%s", apb);
	
	len = strlen(apb);
	
	for(int i=0; i<len; i++) {

		for(int ascii=65; ascii < 91; ascii++) if(ascii==apb[i]) count[ascii]++;
		
		for(int ascii=97; ascii < 123; ascii++) if(ascii==apb[i]) count[ascii-32]++;
		
	}
	
	for(int ascii=65; ascii<91; ascii++)
	if(count[ascii] > max) {
		max = count[ascii];
		max_apb = ascii;
	}
	
	for(int ascii=65; ascii<91; ascii++) if(max == count[ascii]) div++;
	
	if(div > 1) printf("?");
	else printf("%c", max_apb);
	
}
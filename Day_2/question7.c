#include<stdio.h>
int main(){
    int num, r, product = 1;

    printf("Enter the number to find product of their digit: ");

    scanf("%d",&num);

    while(num>0){
        r = num%10;
        product = product *r;
        num = num/10;

    }
    printf("the product obtained is: %d", product);
    return 0;
}
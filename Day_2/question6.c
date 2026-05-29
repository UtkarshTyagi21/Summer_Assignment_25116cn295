#include<stdio.h>
int main()
{
    int num, num2 = 0, r;

    printf("Enter the number to reverse:");

    scanf("%d", &num);

    while(num>0){

        r=num%10;
        num2 = num2*10 + r;
        num=num/10;
    }

    printf("the numer after reversing the digit we get is %d",num2);
    return 0;
    
}
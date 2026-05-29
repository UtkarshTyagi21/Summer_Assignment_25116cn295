#include<stdio.h>
int main()
{
    int num, num2 = 0, r,n;

    printf("Enter the number to reverse:");

    scanf("%d", &num);

    n = num;
    
    while(num>0){

        r=num%10;
        num2 = num2*10 + r;
        num=num/10;
    }

    if(n==num2)
    {
    printf("The entered number is a Paindrome");
    }

    else
    {       
     printf("The entered number is not a Paindrome");
    }
    
    return 0;
}
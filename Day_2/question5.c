#include<stdio.h>
int main()
{ int num ,r,sum=0;

    printf("enter the number for which you want to add the didgit: ");

    scanf("%d",&num);

    while(num > 0){
        
        r = num%10;
        sum = sum + r;

        num=num/10;
        
    }
    printf("The sum of digits in the number is: %d", sum);
    
    return 0;
}
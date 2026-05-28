#include<stdio.h>
int main(){
    int n,i,r,sum=0;
    printf("enter the number, for which you want to count the digit: ");
    scanf("%d",&n);

    while(n>0){

        r=n%10;
        sum=sum+r;
        n=n/10;
    }
    printf("The sum of digits of the number is: %d", sum);
    
    return 0;
}
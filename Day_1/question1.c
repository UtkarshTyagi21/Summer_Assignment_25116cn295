#include<stdio.h>
int main(){
    int n, sum=0, i=0;

    printf("Enter the number you want till you wanted to find the sum: ");

    scanf("%d",&n);

    while(i<=n){

        sum = sum+i;

        i++;
    }
    
    printf("the sum of N natural numbers is: %d", sum);
    return 0;
}
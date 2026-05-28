#include<stdio.h>
int main()
{
    int n, i;
    printf("enter the number to print that table ");
    scanf("%d", &n);
    i=1;
    while (i<=10)
    {
        printf("%d X %d = %d\n", n,i,n*i);
        i=i+1;
    }

printf("The required table ");
return 0;


}
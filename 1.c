#include<stdio.h>
int main()
{
 int a ;
 
 printf("Enter Integer : ");
 scanf("%d" ,&a);

 if(a %2 == 0)
   {
    printf("Even Number \n");

   }
else if(a %2 == 1)
   {
     printf("Odd Number \n ");
   }
return 0;
}

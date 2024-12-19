#include<stdio.h>
int main()
{
  int number,rem;
  number = 5;
  rem = number % 2;
  if(rem == 0){
    printf("The number is even\n");
  }
  else{
    printf("The number is odd\n");
  }

   return 0;
}
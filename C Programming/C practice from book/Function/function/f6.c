#include<stdio.h>
int addNumbers(int number1,int number2);
int main(){
    int result = addNumbers(8,9);
    printf("Result = %d",result);
    return 0;
}
int addNumbers(int number1,int number2){
    int sum = number1 - number2;
    return sum;
    printf("After Return");
}
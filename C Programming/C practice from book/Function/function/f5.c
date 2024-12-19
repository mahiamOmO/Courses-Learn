#include<stdio.h>
int addNumber(int number1,int number2){
    int sum = number1 - number2;
    return sum;
}
int main(){
    int result = addNumber(8,9);
    printf("Result = %d",result);

    return 0;
}
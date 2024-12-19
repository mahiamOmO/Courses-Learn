#include<stdio.h>
int main(){
    int age = 25;
    printf("%p",&age);
    int *ptr = &age;

    printf("\n%p",ptr);

    return 0;
    
}
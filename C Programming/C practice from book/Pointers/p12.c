#include<stdio.h>
int main(){
    int age = 25;
    int *ptr = &age;
    printf("Address: %p\n",ptr);
    printf("Value: %d",ptr);

    return 0;
}
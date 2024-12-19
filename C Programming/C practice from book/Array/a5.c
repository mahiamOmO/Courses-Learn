#include<stdio.h>
int main(){
    int ara[4] = {5,10,15,20};

    ara[0] = 100;
    ara[2] = 200;
    ara[3] = 300;

    printf("%d,%d,%d\n",ara[0],ara[1],ara[2],ara[3]);

    return 0;
}
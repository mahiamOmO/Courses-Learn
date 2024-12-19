#include<stdio.h>
int main(){
    int arr[2][3] = {{1,3,5},{2,4,6}};
    arr[0][2] = 7;
    arr[1][1] = 8;
    printf("%d\n",arr[0][2]);
    printf("%d\n",arr[1][1]);

    return 0;
}
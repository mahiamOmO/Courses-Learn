#include<stdio.h>
int main(){
    int A[5],sum=0;
    for(int i=0;i<5;i++){   //array_summation
        scanf("%d",&A[i]);
    }
    for(int i=0;i<5;i++){
        sum=sum+A[i];
    }
    printf("%d\n",sum);
}
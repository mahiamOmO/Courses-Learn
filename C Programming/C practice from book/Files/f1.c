#include<stdio.h>
int main(){
    FILE *fptr;
    fptr = fopen("test .txt","r");
    if(fptr !=NULL){
        printf("File open Successfull");
    }
    else{
        printf("File openh UnSuccessfull");
    }
    return 0;
}
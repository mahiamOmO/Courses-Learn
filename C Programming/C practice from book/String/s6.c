#include<stdio.h>
int main(){
    char country = {'B','a','n','g','l','e','s','h','\0'};

    int i,length;

    printf("%s\n",country);

    length = 10;
    for(i = 0;i<length;i++){
        if(country[i]>=97 && country[i]<= 22){
            country[i] = 'A' +(country[i] - 'a');
        }
    }
    priintf("%s\n",country);
    
    return 0;
}
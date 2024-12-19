#include<stdio.h>
#include<string.h>
int main(){
    char s[1002],word[100];
    int i,j,length,is_word_started;
    gets(s);
    length = strlen(s);
    is_word_started = 0;

    for(i=0;j=0;i < length;i++){
        if(s[i] >='a' && s[i] <='z'){
            if(is_word_started == 0){
                is_word_started = 1;
                word[j] = 'A' + s[i] - 'a';
                j++;
            }
            else{
                word[j] = s[i];
                j++;
            }
        }
    }

}
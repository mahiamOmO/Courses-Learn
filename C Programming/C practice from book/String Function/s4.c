#include<stdio.h>
#include<string.h>
int main(){
    char text1[] = "Hey, ";
    char text2[] = "How are you?";

   strcat(text1,text2);

   printf("%s",text1);
   return 0;

}
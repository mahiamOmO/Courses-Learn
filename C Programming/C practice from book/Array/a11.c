#include<stdio.h>
int main(){
    int tota_marks[] = {86,78,94,68,92,78,64,,62,72,61,72,66,65,65,80,72,62,68,81,62,66,76,70,77,68,89
    };

    for(marks = 50;marks<=100;marks++){
        count = 0;
        for(i=0;i<40;i++){
            if(total_marks[i] == marks){
                count++;
            }
         }
         printf("Marks: %d Count: %d\n",marks,count);
    }
    return 0;
}
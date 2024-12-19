#include<stdio.h>
#include<string.h>

struct nametype{
    char first[20];
    char last[20];
};

struct studenttype{
    int id;
    struct nametype name;
};
int main(){
    struct studentype student[5];
    int i,n = 5;
    for(i =o;i<n;i++){
        printf("Enter the ID for student %d:",i+1);
        scanf("%d",&student[i].id);
        printf("Enter the first name for student %d:",i+1);
        
    }
}
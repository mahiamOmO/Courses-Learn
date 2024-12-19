#include<stdio.h>
int main(){

int arr[2][3] = {{1,3,5},{2,4,6}};
for(int i=0;i<2;i++){
    for(int j=0;j<3;j++){
        printf("%d\n",arr[i][j]);
    }
}
return 0;

}
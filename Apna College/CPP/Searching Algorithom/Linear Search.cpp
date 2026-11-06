//arr size = 7; target = 8, arr = {4,2,7,8,1,2,5}
#include<iostream>
using namespace std;

int LinearSearch(int arr[],int size,int target){
    for(int i=0;i<size;i++){
        if(arr[i]==target){ //found
            return i; 
        }
    }
    return-1; //not found
}
int main(){
    int arr[] = {4,2,7,8,1,2,5};
    int size = 7;
    int target = 8;
    cout << LinearSearch(arr,size,target) << endl;

    return 0;

}
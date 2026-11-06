#include<iostream>
using namespace std;
int main(){
    int smallest = INT_MAX;
     for(int i=0;i<size;i++){ //min,max
        if(nums[i] < smallest){
            smallest = nums[i];
        }
        smallest = min(num[i],smallest);
     }
     cout << "smallest= " << smallest << endl;
     return 0;

}
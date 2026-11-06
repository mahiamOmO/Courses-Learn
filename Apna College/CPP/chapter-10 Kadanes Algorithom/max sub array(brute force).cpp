#include<iostream>
#include<vector>
using namespace std;
int main(){
    int n = 5;
    int arr[5] = {1,2,3,4,5};

    int maxSum = INT_MIN; 
    
    for(int st=0; st<n; st++){
        int currSum = 0;
        for(int i=st;i<=end;i++){
            currSum += arr[end];
            maxSum = max[crrSum,maxSum];
        
        }
        cout <<"max subarray sum = " << maxSum << endl;
    
    }

}
 return 0;
#include<iostream>
#include<vector>
using namespace std;

// Function outside main
vector<int> pairSum(vector<int> nums, int target){
    vector<int> ans;
    int n = nums.size();

    for(int i=0; i<n; i++){
        for(int j = i+1; j<n; j++){
            if(nums[i] + nums[j] == target){
                ans.push_back(i); // store index i
                ans.push_back(j); // store index j
                return ans; // return immediately after finding the pair
            }
        }
    }
    return ans; // return empty if no pair found
}

int main(){
    vector<int> nums = {2,7,11,15};
    int target = 9;

    vector<int> ans = pairSum(nums, target);

    cout << ans[0] << " , " << ans[1] << endl;

    return 0;
}

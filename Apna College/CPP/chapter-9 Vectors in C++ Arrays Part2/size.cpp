#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> vec;

    vec.push_back(25);
    vec.push_back(35);
    vec.push_back(45);


   cout << vec.size() <<endl;//3
   cout << vec.capacity() <<endl;//4

    return 0; 
}

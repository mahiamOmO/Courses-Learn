#include<iostream>
using namespace std;
int main(){
    double x =4;
    x = x + 0.7;
    cout<<"x = "<<static_cast<int>(x);
    cout<<"The original x = "<<x<<endl;
    return 0;
}
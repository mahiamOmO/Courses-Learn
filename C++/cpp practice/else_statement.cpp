#include<iostream>
using namespace std;
int main(){ 
    int temp;
    cout<<"Enter Today's temperature"<<endl;
    cin>>temp;
    if(temp>50){
        cout<<"Please turn the fan on."<<endln;
    }
    else if(temp<20){
        cout<<"Turn the heater on";
    }
    else{
        cout<<"No need for fan";
    }
}
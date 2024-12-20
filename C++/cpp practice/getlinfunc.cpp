#include<iostream>
#include<string>
using namespace std;
int main(){
    string first_name;
    string last_name;
    cout<<"Enter your first name : ";
    cin>>first_name;
    cout<<"Enter your middle and last name: ";
    getline(cin,last_name);

    cout<<"First name: "<<first_name<<endl;
    cout<<"Middle and Last name: "<<last_name;
    return 0;
}
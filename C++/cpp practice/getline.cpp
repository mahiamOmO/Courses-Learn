#include<iostream>
#include<string>
using namespace std;

int main(){
    string first_name;
    cout << "Enter your first name: ";
    getline(cin, first_name);

    cout << "Hi " << first_name;
    return 0;
}

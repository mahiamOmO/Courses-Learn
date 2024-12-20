#include<iostream>
using namespace std;

int main() {
    bool x;
    int a;
    cout << "Enter a number: " << endl;
    cin >> a;
    x = a > 5;
    if(x) {
        cout << "Hi" << endl;
    } else {
        cout << "Condition is false" << endl;
    }
    return 0;
}

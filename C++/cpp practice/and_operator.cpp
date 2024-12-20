#include<iostream>
using namespace std;

int main() {
    int x;
    int age;
    cout << "Enter your favorite number: ";
    cin >> x;
    cout << "Enter your age: ";
    cin >> age;
    
    if ((x == 7) && (age == 17)) {
        cout << "Congratulations!!" << endl;
        cout << "You won" << endl;
    } else {
        cout << "Sorry, you didn't win" << endl;
    }

    return 0;
}

#include<iostream>
using namespace std;

int main(){
    int a;
    cout << "Welcome to our program! What would you like to do?" << endl;
    cout << "1. Create a new file." << endl;
    cout << "2. Open a file." << endl;
    cout << "3. Upload a file." << endl;
    cout << "4. Exit." << endl;
    cin >> a;
    
    switch(a) {
        case 1: 
            cout << "A file has been created." << endl;
            break;
        case 2: 
            cout << "Which file to open?" << endl;
            break;
        case 3: 
            cout << "Choose a file to upload (max: 4MB)." << endl;
            break;
        case 4: 
            cout << "Thank you!!" << endl;
            break;
        default:
            cout << "Please enter either 1, 2, 3, or 4." << endl;
            break;
    }
    return 0;
}

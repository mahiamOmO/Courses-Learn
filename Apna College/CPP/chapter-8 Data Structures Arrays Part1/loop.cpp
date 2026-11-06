#include<iostream>
using namespace std;
int main() {
    int marks[5] = {99,88,87,36,54};
    int size = 5;

    for(int i=0;i<size;i++){
        cin >> marks[i];
    }
    //loops : 0 to size-1
    for(int i=0;i<size;i++){
        cout << marks[i] <<endl;
    }


    return 0;
}
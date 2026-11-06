#include<iostream>
using namespace std;

int main() {
    int n = 4;
    int num = 1;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }

    cout << "after pattern: " << num << endl;

    return 0;
}

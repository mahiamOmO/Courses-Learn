#include<iostream>
using namespace std;

int main() {
    int n = 4;

    for(int i = 0; i < n; i++) {
        // spaces: n-i-1
        for(int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }

        // left numbers: 1 to i+1
        for(int j = 1; j <= i + 1; j++) {
            cout << j;
        }

        // right numbers: i to 1
        for(int j = i; j >= 1; j--) {
            cout << j;
        }

        cout << endl; // move to the next line
    }

    return 0;
}

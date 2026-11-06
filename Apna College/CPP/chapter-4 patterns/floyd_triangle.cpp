#include<iostream>
using namespace std;

int main() {
    int n = 4;

    int num = 1;

    for(int i = 0; i < n; i++) {
        for(int j=i+1; j>0; j--) { //backwards => i+1
            cout << num <<" ";
            num++;
        }
        cout << endl;
    }
    return 0;
}

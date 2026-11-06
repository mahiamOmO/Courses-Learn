#include<iostream>
using namespace std;

int factorial N(int n) {
    int fact= 1;
    for(int i = 1;i<=N;i++){
        fact *= i;
    }
    return fact;
}

int main() {
    cout << factorial N(5) << endl;
    cout << factorial N(10) << endl;
    return 0;
}

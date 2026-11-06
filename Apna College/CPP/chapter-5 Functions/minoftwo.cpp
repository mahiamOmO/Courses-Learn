#include<iostream>
using namespace std;

double sum(double a, double b) {
    double s = a + b;
    return s;
}

int minOfTwo(int a, int b) {  // parameters
    if(a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    cout << "min = " << minOfTwo(5, 3) << endl;  // arguments are pass by value
    return 0;
}

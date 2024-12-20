#include <iostream>
#include <cmath>  // Include cmath for the pow function

using namespace std;

int main() {
    double x = 2.0;
    double a;
    a = pow(x, 2);  // Added the missing semicolon
    cout << a << endl;  // Output the result
    return 0;
}

#include <iostream>
using namespace std;

int main() {
    int a;
    a = 12;
    cout << "Size of int: " << sizeof(a) << " bytes" << endl;

    float b;
    cout << "Size of float: " << sizeof(b) << " bytes" << endl;

    char c;
    cout << "Size of char: " << sizeof(c) << " bytes" << endl;

    bool d;
    cout << "Size of bool: " << sizeof(d) << " bytes" << endl;

    return 0;
}

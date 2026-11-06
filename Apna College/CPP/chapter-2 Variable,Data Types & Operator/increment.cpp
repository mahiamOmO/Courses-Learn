#include<iostream>
using namespace std;
int main() {
    int a = 10;

    int b = a++; //post increment 
    // Post-increment use kora hoise
    // Step 1: a er current value (10) b te assign hoy
    // Step 2: a er value ekbar increment hoy (a = 11)

    int b = ++a;
    // Pre-increment use kora hoise
    // Step 1: a er value ekbar increment hoy (a = 11)
    // Step 2: updated a er value (11) b te assign hoy
    cout<< "b = " << b << endl; //10
    cout<<"a = "<< a <<endl; //11
    return 0;
}

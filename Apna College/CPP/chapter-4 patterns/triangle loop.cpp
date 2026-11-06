#include<iostream>
using namespace std;

int main() {
    int n = 10;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j <i+1; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
output:
*
***
***
*****
**********
***********
************
*************
**************
***************
// Explanation: The outer loop runs 'n' times, and for each iteration of the outer
// loop, the inner loop runs 'i+1' times, where 'i' is the current iteration of the outer loop.
// This results in printing the asterisks '*' for 'i+1' times in each row.
// The first row prints '*', the second row prints '**', the third row prints '***', and so on.
// The output is a right-angled triangle pattern of asterisks.
// The pattern is formed by printing the asterisk '*' repeatedly for each
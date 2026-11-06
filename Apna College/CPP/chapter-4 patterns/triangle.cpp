#include<iostream>
using namespace std;

int main() {
    int n = 4;

    for(int i = 0; i < n; i++) {        
        for(int j = 0; j <i+1; j++) {
            cout << (i+1);
        }
        cout << endl;
    }
    return 0;
}
output:
1
22
333
4444
// Explanation: The outer loop runs 'n' times, and for each iteration of the outer
// loop, the inner loop runs 'i+1' times, where 'i' is the current iteration of the outer loop.
// This results in printing the number 'i+1' for 'i+1' times in each row.
// The first row prints '1', the second row prints '22', the third row prints '333', and the fourth row prints '4444'.
// The output is a right-angled triangle pattern of numbers.
// The pattern is formed by printing the row number repeatedly for each row.
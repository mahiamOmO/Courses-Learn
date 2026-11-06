#include<iostream>
using namespace std;

int main() {
    int n = 4;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << " * ";
        }
        cout << endl;
    }
    return 0;
}
output:
 *  *  *  * * 
 *  *  *  * * 
 *  *  *  * * 
 *  *  *  * *
// Explanation: The outer loop runs 'n' times, and for each iteration of the outer
// loop, the inner loop runs 'n' times.
// This results in printing the asterisk '*' for 'n' times in each row.
// The first row prints ' *  *  *  * ', the second row prints ' *  *  *  * ', and so on.
// The output is a square pattern of asterisks.
// The pattern is formed by printing the asterisk '*' repeatedly for each row, resulting
// in a square shape with 'n' rows and 'n' columns of asterisks.
// The spaces around the asterisks are included to maintain the square shape and improve readability
// of the output.
// The output is a square pattern of asterisks, where each row contains 'n' asterisks separated by spaces.
// The pattern is formed by printing the asterisk '*' repeatedly for each row, resulting in a square shape with 'n' rows and 'n' columns of asterisks.
// The spaces around the asterisks are included to maintain the square shape and improve readability of the output.
// The output is a square pattern of asterisks, where each row contains 'n' asterisks separated by spaces.
// The pattern is formed by printing the asterisk '*' repeatedly for each row, resulting in a square shape with 'n' rows and 'n' columns of asterisks.
// The spaces around the asterisks are included

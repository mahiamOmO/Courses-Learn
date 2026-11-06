#include<iostream> 
using namespace std;
int main() {
    char grade = 'a'; //97  //// 'b' = 98, 'A' = 65, '0' = 48, ' ' (space) = 32

    int value = grade;   // implicit type conversion small to big

    cout << value << endl;
   
    
    return 0;
    
}
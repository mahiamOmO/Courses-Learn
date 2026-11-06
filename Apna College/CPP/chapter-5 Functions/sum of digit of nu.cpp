#include<iostream>
using namespace std;

int sumofDigits(int num) {
    int digSum = 0;
    while(num > 0) {                 // 145 hoche number ekbar modulo korbo last digit pawar jonno arekbar divide korbo bakituku pawar jonno
        int lastDig = num % 10;   // শেষ সংখ্যা বের করি
        num /= 10;                // সংখ্যা ছোট করি
        digSum += lastDig;        // যোগ করি
    }
    return digSum;
}

int main() {
    cout << "sum = " << sumofDigits(2356) << endl;
    return 0;
}

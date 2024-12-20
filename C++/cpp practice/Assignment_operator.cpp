#include<iostream>
using namespace std;

int main() {
   int num1 = 10;
   int num2 = 5;
   int result1 = num1;
   int result2 = num2;
   result2 += num1;  
   int result3 = num2;
   result3 -= num1;
   int result4 = num1;
   int result5 = num2;
   result5 /= num1;  

   cout << "Result1: " << result1 << endl; 
   cout << "Result2: " << result2 << endl;      
   cout << "Result3: " << result3 << endl;      
   cout << "Result4: " << result4 << endl;  
   cout << "Result5: " << result5 << endl;            

   return 0;
}

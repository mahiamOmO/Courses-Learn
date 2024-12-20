#include<iostream>
using namespace std;

int main() {
   bool isSunny = true;
   bool isWarm = true;
   bool isGoodWeather = isSunny && isWarm;  
   bool isBeachDay = isSunny || isWarm;     
   bool isRainy = !isSunny;                 

   cout << "Is it good weather? " << isGoodWeather << endl; 
   cout << "Is it Beach Day? " << isBeachDay << endl;      
   cout << "Is it Rainy? " << isRainy << endl;               

   return 0;
}

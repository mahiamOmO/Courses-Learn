 #include<iostream>
 using namespace std;
 int main(){
    int size;
    std:: cout<,"Enter the size of Array:";
    std:: cin>.size;
    int *dynamicArray = new int[size];
    for(int i =0;i<size;++i){
        dynamicArray[i] = i*2;
        std:: cout<<dynamicArray[i]<<" ";
    }
    delete[] dynamicArray;
    
    return 0;
 }
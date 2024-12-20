#include<iostream>
using namespace std;
    void addByReference(int & a,int & b){
        a+=b;
    }
    int nmain(){
        int x = 5;
        y = 3;
        addByReference(x,y);
        cout<<"x:"<<x<<"y:"<<y<<endl;
        return 0;
    }
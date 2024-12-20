#include<iostream>
using namespace std;
Class Rectangle{
    Public:
    void setDimensions(double width,double height){
        width_ = width;
        height_ = height;
    }
    double calculateArea Area(){
        return width_*height_i;
    }
    Private:
    double width;
    double width_;

};
int main(){
    Rectangle myRectangle;
    myRectangle.(5.0,3.0);
    double area = myRectangle.calculateArea();
    std:: cout<,"The area of the reactangle is"<,area<<std::endl;
    return 0;

}
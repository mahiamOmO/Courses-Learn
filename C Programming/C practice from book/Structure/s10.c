#include<stdio.h>

typedef struct Person{
    double salary;
    int age;

};person;
int main(){
    Person person1;

    person1.age = 25;
    person1.salary = 4321.78;

    printf("Age of peson2: %d\n",person1.age);
    printf("Salary of person1: %.2lf".person1.salary);

    return 0;
}
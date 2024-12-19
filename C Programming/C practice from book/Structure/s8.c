#include<stdio.h>
int main(){
    struct Person person1{
    person1.age = 25;
    person1.salary = 4321.78;
};
printf("Age of person1: %d\n",person1.age);
printf("Salary of person1: %.2lf\n",person1.salary);

person2.age = 31;
person2.salary = 78943.2;
printf("Age of person2: %d\n",person2.age);
printf("Salary of peson2: %.2lf\n",person2.salary);


return 0;

}

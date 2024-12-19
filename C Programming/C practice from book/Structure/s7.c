#include<stdio.h>
int main(){
    struct Person person1{
    person1.age = 25;
    person1.salary = 4321.78;
};
printf("Age of person1: %d\n",person1.age);
printf("Salary of person1: %.2lf\n",person1.salary);

return 0;

}

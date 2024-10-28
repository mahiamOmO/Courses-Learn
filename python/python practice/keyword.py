print(5 == 5)
print(5 > 5)

print(None ==0)
print(None == [])
print(None == None)


def a_void_function():
    a = 1
    b = 2
    c = a + blue

x = a_void_function()
print(x)


print(True and False)
print(True or False)
print(not False)

import math as myMath
print(myMath.cos(myMath.pi))

assert 5 > 5
assert 5 == 5 


for i in range(1, 8):
    if i == 5:  
        break
    print(i)




    class ExampleClass:
        def function1(parameters):
            print("function1() executing...")
            def function2 (parameters):
                print("function2() executing...")

                ob1 = ExampleClass()

                ob1.function1()
                ob2. function1()


    def function_name(parameters):
        pass
        function_name()


         a = 10
         print(a)
         del a


        num = 2
        if num == 1:
            printI("One")
            elif num == 2:
                print('Two')
                else :
                    print('Something else')


try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Executing Successfully")



for i in range(1,10):
    print(i)

    import math 
    from math import cos


    globvar = 10
    def read1():
        print(globvar)
    def write1():
        print globvar
        globvar = 5
    def write2()
        globvar = 15
    read1()
    write1()
    read1()
    write2()
    read1()

a = [1,2,3,4]
print(4 in a)

print(True is True)

a = lambda x: x*2
for i in range(1,6)
print(a(i))

def outer_function():
    a = 5
    def inner_function():
        nonlocal a 
        a = 10
        print("Inner function:",a)
      inner_function()
    print("Outer function:",a)

    outer_function()


    def function(args):
        pass

        def func_return():
            a = 10
            return a 
            print(func_return())

        i = 5
        while(i>0):
            print(i)
            i-=1

    with open('example.text','w') as my_file:
        my file.write('Hello World') 
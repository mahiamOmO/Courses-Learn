class example:
    def add(self,a,b):
        x = a+b
        return x
    def add(self,a,b,c):
        x = a+b+c
        return x
    obj = example()

    print(obj.add(10,20,30))
    print(obj.add(10,20))


class Calculate:
    def add(self): #removed
        x=10
        y=20
        z=x+y
    def add(self,a,b):
        return a+b
    def add(self,x,y):
        a=x
        b=y
        c=a+b
        print(c)
c=Calculate() #in python traditional method overloading is not posible
c.add(10,20)

class Calculate:
    def __init__(self): #removed
        x=10
        y=20
        z=x+y
    def __init__(self,a,b):
        return a+b
    def __init__(self,x,y):
        a=x
        b=y
        c=a+b
c=Calculate(10,20) #in python constructor overloading is not posible the 
print(c)



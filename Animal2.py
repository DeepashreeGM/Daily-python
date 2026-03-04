class Animal:
    def eat(self):
        print("All animals   will eat")
class Dog(Animal):
    def bark(self):
        print("Dog is Barking")
class Cat(Animal):
    def meow(self):
        print("cat make sound meow")
class Lion(Animal):
    def roar(self):
        print("Lion roars")

l=Lion()
print("********Lion property********")
l.roar
l.eat()
c=Cat()
print("********Cat property********")
c.meow()
c.eat()
print("********Dog property********")
d=Dog()
d.eat()
print("********Animal property********")
a=Animal()
a.eat()
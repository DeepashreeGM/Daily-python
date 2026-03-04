class Animal:
    def eat(self):
        print("All animals   will eat")
class Dog(Animal):
    def bark(self):
        print("Dog is Barking")
class BabyDog(Dog):
    def weep(self):
        print("Baby Dog is weeping")
b=BabyDog()
print("********Baby dog property********")
b.weep()
b.bark()
b.eat()
print("********Dog property********")
d=Dog()
d.bark()
d.eat()
print("********Animal property********")
a=Animal()
a.eat()
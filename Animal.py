class Animal:
    zoo="City Zoo"
    def __init__(self):
        self.species="Mammal" #we can inherite instance veriable
    def sleep(self):
        print("Animal Is Sleeping")#we can invoke instance method
    @classmethod
    def eat(cls):
        print("Animal is eating") #we can invoke class method
    @staticmethod
    def dance():
        print("Animal is standing")#we can inherite static method
class Dog(Animal):
    def bark(self):
        print("Barking") #We can inherite static method
dog1=Dog()
print(dog1.species)
print(Dog.zoo)
dog1.sleep()
dog1.bark()
Dog.eat()
Dog.dance()
#we cannont inherite local variables
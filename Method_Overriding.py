class Animal:
    def makeSound(self):
        print("All Animal makes sound")
class Dog(Animal):
    def makeSound(self):
        print("Bow Bow")
d=Dog()
d.makesound() 
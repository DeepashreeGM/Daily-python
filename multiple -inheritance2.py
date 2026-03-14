class Father:
    def drive(self):
        print("Father Knows how to deive")

class Mother:
    def drive(self):
        print("Mother knows how to drive")

class Son(Father,Mother):#Sub class of Mother And Father
    def play(self):
        print("Knows how to play")

class Daughter (Mother,Father): #Sub class of Mother And Father
    def read(self):
        print("Knows how to read") 
s=Son()
s.play()
s.drive()
'''Both super class Father and Mother has a method feature Drive in this case the sub classes will
        will follow the MRO C3 agorithm in which the left cls properties will be inherited first'''
d=Daughter()
d.drive()
d.read()

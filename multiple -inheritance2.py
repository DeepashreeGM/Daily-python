class Father:
    def drive(self):
        print("Father Knows how to deive")
class Mother:
    def drive(self):
        print("Mother knows how to drive")
class Son(Father,Mother):
    def play(self):
        print("Knows how to play")
class Daughter (Mother,Father):
    def read(self):
        print("Knows how to read") 
s=Son()
s.play()
s.drive()
d=Daughter()
d.drive()
d.read()

class Father:
    def drive(self):
        print("Knows how to deive")
class Mother:
    def cook(self):
        print("knows how to cook")
class Son(Father,Mother):
    def play(self):
        print("Knows how to play")
class Daughter (Father,Mother):
    def read(self):
        print("Knows how to read") 
s=Son()
s.play()
s.cook()
s.drive()
print("*************")
d=Daughter()
d.read()
d.cook()
d.drive()
class Car:
    wheels=4
    def __init__(self):
        self.brand=None
    def show(self):
        print("Brand name is:",self.brand)
        print("number of wheels:",self.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car()
c1.brand="TATA"
c1.show()
c1.change_wheels(8)
c1.show()
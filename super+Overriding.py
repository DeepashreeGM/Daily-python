class SmartPhone:
    def takePhoto(self):
        print("Taking a normal photo")
class iPhone(SmartPhone):
    def takePhoto(self):#Overriding the parent class method
        super().takePhoto()#using super() keyword to use the parent class method behavior
        print("Taking a 48mp photo")
i=iPhone()
i.takePhoto() #Now it prints both behavior
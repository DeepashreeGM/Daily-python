class Test:
    def __init__(self):
        self.x=10
        self.__y=20
class RunTest:
    def run(self):
        test=Test()
        print("Public variable x:",test.x)
        print("Private variable y:",test._Test__y)#we can acces the private variable by name mangling 
        print(test.__dict__)#this shows how the variables stored in dictionary
        #print("private Variable y:",test.__y)-This will give an error 
r=RunTest()
r.run()

class BookMyshow:
    def makepayment(self):
        print("payment sone successfull")
b=BookMyshow()
print(b.__dict__)
b.makepayment()
print(b.__class__)
print(b.__class__.__dict__)
print(b.__class__.__dict__["makepayment"])
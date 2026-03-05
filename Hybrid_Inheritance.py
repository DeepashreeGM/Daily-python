class A:
    def display(self):
        print("Displaying A")
class B(A):
    def run(self):
        print("Runs B")
class C(A):
    def runner(self):
        print("Runner is C")
class D(B,C):
    def read(self):
        print("D is Reading")
d=D()
d.read()
d.runner()
d.run()
d.display()
print("**********C Property***********")
c=C()
c.runner()
c.display()
print("**********B Property***********")
b=B()
b.run()
b.display()
print("**********A Property***********")
a=A()
a.display()

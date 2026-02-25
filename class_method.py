class DMART:
    discount_on_each_product=0.10
    def __init__(self):
        self.gstn=None
        self.location=None
    def calculatediscount(self,product_name,org_productprice):
        actual_price=org_productprice-(org_productprice* DMART.discount_on_each_product)
        print("Actual Price of", product_name, "after discount ---->", actual_price)
    @classmethod
    def revised_discount(cls,new_discount):
        cls.discount_on_each_product=new_discount
    @staticmethod
    def frisktheCustomer():
        print("Cutermer are checked and validated")
print("**********Calling Static Mathod**********")
DMART.frisktheCustomer()
print("**********PRICE WITH DEFAULT DISCOUNT***********")
d1=DMART()
d1.gstn=12345567
d1.location="BTM"
d1.calculatediscount("DARK FANTACY", 350)

d2=DMART()
d2.gstn=455671011
d2.location="MAJESTIC"
d2.calculatediscount("HIDE&SIKE", 450)
d1.revised_discount(0.20)
print("**********PRICE WITH REVISED DISCOUNT DUE TO FESTIVAL***********")
d1.calculatediscount("DARK FANTACY", 350)
d2.calculatediscount("HIDE&SIKE", 450)

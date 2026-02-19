class Test:
    def Verifyuser(func_name):
        def wrapper_name(self):
            print("Verified successfully")
            func_name(self)
            print("user has completed the operation, logged out successfully")
        return wrapper_name
    @Verifyuser
    def starttest(self):
        print("test started")
    
    @Verifyuser
    def collecthallticket(self):
        print("hallticket collected successfully")
t1=Test()
t1.collecthallticket()
t1.starttest()
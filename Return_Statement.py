class skyscanner:
    def searchflight(self,source,destination):
        noofflight=1
        nameofflight="indigo"
        return "No Of Flight is" , noofflight, "name is", nameofflight
s=skyscanner()
s.searchflight("Banglore","Rammandhir")
#Option one
flight=s.searchflight("Banglore","Rammandhir")
print(flight)
#option two 
print(s.searchflight("Banglore","Rammandhir"))
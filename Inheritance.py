"""#1.Single type inheritance

class lowlevellanuage:
    def understanding(self):
        print("machine high")
        
class highlevellanuage(lowlevellanuage):
    def  understandingcapacity (self):
        print("machine low")

l=lowlevellanuage()
l.understanding()"""

"""#2.Multilevel inheritance

class lowlevellanuage:
    def grandfather(self):
        print("Fortran")
        
class midlevellanuage(lowlevellanuage):
    def father(self):
        print("Algol 60")

class highlevellanuage(midlevellanuage):
    def son(self):
        print("Algol 68")

l=highlevellanuage()
l.father()"""


"""#3.Multiple inheritance

class highlevellanuage:
    def python(self):
        print("SUPPORTS")

class lowlevellanuage(highlevellanuage):
    def C(self):
        print("DOES NOT")

class midlevellanuage(lowlevellanuage,highlevellanuage):
    def JAWA(self):
        print("DIAMOND PROBLEM")

L=midlevellanuage()
L.python()
L.JAWA()"""

"""#4.Hierachial inheritance

class computerlanuages:
    def lanuages(self):
        print("UNDERSTANDS")


class understandinglevel(computerlanuages):
    def low(self):
        print("UNDERSTANDS EASYLY")

class understandinglevels(computerlanuages):
    def high(self):
        print("UNDERSTANDS MODERATELY")


L=computerlanuages()
L.low()"""













        









        









































    
    


        

        




















    
    

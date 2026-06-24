"""#1.METHOD OVER RIDING
class doraemon:
    def power(self):
        pass

class takecopter(doraemon):
    def power(self):
        print("FLYING")

class anywheredoor(doraemon):
    def power(self):
        print("TAKES ANYWHERE")

class timemachine(doraemon):
    def power(self):
        print("TAKES TO FUTURE")


class biglight(doraemon):
    def power(self):
        print("MAKES BIG")

doraemon=[timemachine(),biglight(),takecopter(),anywheredoor()]
for doraemon in doraemon:
    doraemon.power()"""

"""#2.METHOD OVER LOADING

class Calculator:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

c=Calculator()
c.add(2,5,3)
c.add(6,9)
c.add(9)"""

#3. USE TYPE CHECKS

class DataProcessor:
    def process(self,data):
        if isinstance(data,list):
            return[x * 5 for x in data]
        elif isinstance(data,str):
            return data.upper()
        return data

d=DataProcessor()
print(d.process([10,20]))
print(d.process("JAYANTH"))














    
























    















    
        

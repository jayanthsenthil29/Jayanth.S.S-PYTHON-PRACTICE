"""#1.GET
SAS = {"name":"jhon price","age":45,"role":"captain of task force 141"}
print(SAS.get("age"))

#2.KEY
SAS = {"name":"jhon price","age":45,"role":"captain of task force 141"}
print(SAS.keys())

#3.VALUES
SAS = {"name":'jhon "soap" mactavish',"age":35,"role":"sniper-demolitions","status":"KIA"}
print(SAS.values())

#4.ITEMS
SAS = {"name":'kyle "GAZ" garrick',"age":37,"role":"tactical specialist, interrogator"}
print(SAS.items())"""

"""#5.UPDATE
SAS = {"name":'simon "ghost" riley',"age":40,"role":"operations specialist and second-in-command "}
SAS.update({"age":42})
print(SAS)"""

"""#6.POP
RANGERS = {"name":'Hershel von Shepherd III',"age":60,"role":"GENERAL","call sign":"GOLD EAGLE"}
X = RANGERS.pop("call sign")
print(X)
print(RANGERS)"""

"""#7.POP ITEM
RANGERS = {"name":'Hershel von Shepherd III',"age":60,"role":"GENERAL","call sign":"GOLD EAGLE"}
print(RANGERS.popitem())"""

"""#8.CLEAR
student = {"name": "John", "age": 20}
student.clear()
print(student)"""


"""#9.COPY
SAS = {"name": "John Price"}
TF141 = SAS.copy()
print(TF141)

#10.SET DEFAULT

DELTA = {"Master Sergeant":"Thomas R"}
DELTA.setdefault("call sign","SANDMAN")
print(DELTA)"""


#11.FROM KEYS

keys = ("a", "b", "c")
d = dict.fromkeys(keys, 0)
print(d)




















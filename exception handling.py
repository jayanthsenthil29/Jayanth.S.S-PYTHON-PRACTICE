"""#1.name error

try:
    K=7
    print(b)
except Exception as e:
    print(e)

finally:
    c=8
    print(c)
    
#2.arithemetic error
    d=1
    e=0
    print(a/b)

#3.type error
age="17"
print(age+1)

#4.Value error
n=int("janaa")
print(n)"""

"""#5.index error
a=[10,20]
print(a[6])"""


"""#6.key error
s={"name":"walter"}
print(s["job"])"""

"""#7.file not found
open("man.txt",'r')

#8.modulenotfound error
import jayanth

#9.stackoverflow error
import math
print(math.exp(1000))

#10.memory error
h=[1]*(10**500)
print(h)"""

"""try:
    a=int(input("enter the num"))
    b=int(input("enter the num"))
    if b==0:
        raise Exception('do not give zero')
    k=a+b 
    j=a-b
    i=a/b
    print(k,j,i)
except Exception as e:
    print(e)

balance=int(input("enter your balance"))
assert balance>0,"balance should be greater than 0"
print("transaction ...")"""


def test_flow():
    try:
        return"From try"
    finally:
        return "From finally"
    print(test_flow())


    try:
        num = int("abc")
        except Exception:
            print("Generic catch")
            expect ValueError:
                print("Specific catch")





            













































































































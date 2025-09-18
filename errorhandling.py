#error handling
#print(x)  # here x is not define so is called name error
try:
    print(x)
except NameError:
    print("x not defined")

#y=1/0
#print(y)  
try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError")

#a="pawan"
#b=int(a)
#print(b)
try:
    a="pawan"
    b=int(a)
    print(b)
except ValueError:
    print("string not cast in int")

#mylist=["mukul","kanak","krsna"]
#print(mylist[4])
try:
    mylist=["mukul","kanak","krsna"]
    print(mylist[4])
except IndexError:
    print("index  out of range")

x="pawan"
y=4
c=x*y
print(c)
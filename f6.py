
def add(a,b):
    #return a+b
    print(f"sum of {a} + {b} = {a+b}")
def sub(a,b):
    #return a-b
    print(f"subtraction of {a} - {b} = {a-b}")
def multiply(a,b):
    #return a*b 
    print(f"multiply of {a} * {b} = {a*b}")
def divide(a,b):
    #return a/b
    print(f"divide of {a} / {b} = {a/b}")
def modulous(a,b):
    print(f"modulous of{a} % {b} = {a%b}")    


print("Operators Value Means-: 1=add  || 2=sub || 3=multiply  || 4=divide || 5=modulous  || 6= break, n>5 is invalid")  
while True:
    n=int(input("enter the value of n for operator:")) 
    if(n>6):
        print("invalid operator! Can't Calculate \U0001f62c")
        continue
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    if(n==1):
        add(a,b)
    elif(n==2):
        sub(a,b)
    elif(n==3):
        multiply(a,b)
    elif(n==4):
        divide(a,b) 
    elif(n==5):
        modulous(a,b)   
    elif n==6:
        break
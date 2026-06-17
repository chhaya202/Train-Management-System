#find the larger number
n1=int(input("enter the value of n1:"))
n2=int(input("enter the value of n2:"))
n3=int(input("enter the value of n3:"))
if (n1>=n2 and n1>=n3):
    print("n1 is greater number")
elif(n2>=n1 and n2>=n3):
    print("n2 is greater number")
elif n3>n1 and n3>n2:
    print("n3 is greater number")       
else:
    print("equal")
    

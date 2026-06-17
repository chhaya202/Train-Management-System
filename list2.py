# list
fruits=["mango","apple","banana","orange"]
print("1=add element  ||  2=remove element  ||  3=break  || n>3=continue")
while True:
 n=int(input("enter the value of n:"))
 if n>3:
     continue
 if n==1:
    fruits.insert(2,"strawberry")
    fruits.append("papaya")
 elif n==2:
    fruits.remove("orange")
    fruits.pop()
    
 elif n==3:
    break
 print(fruits)

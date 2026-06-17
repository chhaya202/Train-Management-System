# sum of only positive number
sum=0
for i in range (10):
    n=int(input("enter the number:"))
    if n<0:
        continue
        #break
    sum +=n
print(f"the sum of positive number:{sum}")    
# collections:

# list- [] index, order, change- add update delete
# tuple- () index order   unchangeable
# set - {} unorder, change- add delete
# dict- {} order index- key value , change

color={"a","b","c","red","pink","blue"}
# print(color[1:5:2])

color.add("green")

# color.append("black")
# color.insert(2,"green")

# color[0]="brown"

color.remove("c")
# del color[1]
# color.pop()

print(color)
print(len(color))
print(type(color))

for i in color:
    print(i)
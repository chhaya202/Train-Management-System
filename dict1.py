student={
    "name":"aman",
    "course":"python"
}
student["marks"]=98
student["name"]="amandeep"
del student['course']

for i,j in student.items():
    print(i,j)

# print(student['name'])
print(student)
print(type(student))
print(len(student))
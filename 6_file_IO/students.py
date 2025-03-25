

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # split the string by the ,
        print(f"{row[0]} is in {row[1]}")

# another version thats more readable
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # split the string by the ,
        print(f"{name} is in {house}")

        
# create list to append
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # split the string by the ,
        student = {"name": name, "house": house} 
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name): # sorted function can use the get_name functions
    print(f"{student['name']} is in {student['house']}")

## can also do this
for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['house']}")
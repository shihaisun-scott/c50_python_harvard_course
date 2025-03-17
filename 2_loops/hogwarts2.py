# Dictionary - curly braces
# [keys: values]
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}

print(students["Hermione"]) # answer will be Gryffindor

for student in students:
    print(student, students[student])

# more data with patronus: list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
] # list of four dictionaries


for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")
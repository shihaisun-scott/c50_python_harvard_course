students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Hufflepuff"}
]


# example 1
gryffindors = [
    student["name"] for students in students if students["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)


# example 2 -- using filter
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindor = filter(is_gryffindor, students)
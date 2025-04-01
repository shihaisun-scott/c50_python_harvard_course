students = ["Hermione", "Harry", "Ron"]

# example 1
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

# example 2
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# example 3
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
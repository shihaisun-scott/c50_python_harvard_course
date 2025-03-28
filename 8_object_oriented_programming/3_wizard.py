# Inheritence: multiple classes can relate to each other (wizard here)
#   borrowing common functionalities from parent functions (super)

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) # accessing the super class (wizard)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # accessing the super class (wizard)
        self.subject = subject
    

wizard = Wizard("Albus")
student = Student("Harry, Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")
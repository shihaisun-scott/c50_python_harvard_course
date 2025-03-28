
class Student(): # define object
    def __init__(self, name, house, patronous): # adding variables to objects
        if not name:
            raise ValueError ("Missing name")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw","Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self): # defining our own function
        match self.patronous:
            case "Stag":
                return "stag emoji"
            case "Otter":
                return "otter emoji"
            case _:
                return "no emoji"


# __init__ to initiate
# self to store to itself
# raise to alert the programmer that there is something wrong
# __str__ to print as a string, else it prints the location of the object in the computer
# classes can have functions/methods built in (e.g., charm)

def main():
    student = get_student()
    print(student)
    print("Expecto patronum")
    print(student.charm())

def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
    return Student(name, house, patronous)

if __name__ == "__main__":
    main()
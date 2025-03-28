
class Student(): # define object
    def __init__(self, name, house): # adding variables to objects
        # if not name: # this is in the setter
        #     raise ValueError ("Missing name")
        # if house not in ["Gryffindor", "Slytherin", "Ravenclaw","Hufflepuff"]: # do not need this after a setter
        #     raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError ("Missing name")
        self._name = name
    
    @property # getter
    def house(self):
        return self._house # the underscore is so there is no collision from self.house above
    @house.setter # setter -- this function will get called if house is redefined
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw","Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house
    

# __init__ to initiate
# self to store to itself
# raise to alert the programmer that there is something wrong
# __str__ to print as a string, else it prints the location of the object in the computer
# classes can have functions/methods built in (e.g., charm)
# properties: attribute to have more control over @property, decorators (functions modifying other functions)
    # i.e., having control over the object so that it can't be changed to an unintended definition

def main():
    student = get_student()
    print(student)

def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
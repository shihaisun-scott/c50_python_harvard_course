
class Student(): # define object
    def __init__(self, name, house): # adding variables to objects
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls): # moved the get_student function here
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get() # this is cleaner now
    print(student)


if __name__ == "__main__":
    main()
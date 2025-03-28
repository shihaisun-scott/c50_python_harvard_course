import random 

class Hat:
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    @classmethod # now a class variable, not a self
    def sort(cls, name): # note always self first
        print(f"{name} in in {random.choice(cls.houses)}")


Hat.sort("Harry")
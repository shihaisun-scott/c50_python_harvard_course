# best practice to not hard-code and use constants instead

# MEOWS = 3 # Cap to indicate to not change

# for _ in range(MEOWS):
#     print("meow")

# inside a class need a variable to not be changed
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()


# type hints: to tell python what type of variable it needs to be
# use mypy to check
# pip install mypy
# mypy meow.py

def meow(n: int) -> None: # needs to be int and returns none
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number) # this will cause an error because it is not an int

meows = str = meow(number)
print(meows) # none because the function does not return a value

## docstrings: document your functions
def meow(n: int) -> str: 
    """Meow n times.""" # triple quotation marks
    return "meow\n" * n

# standard format for documenting your own functions
def meow(n: int) -> str: 
    """
    Meow n times.

    :param n: number of times to meow
    :type n: int
    :raise Type error: If n is not an int
    :return: A string of n meows, one per line
    :rstring: str
    """ # triple quotation marks
    return "meow\n" * n
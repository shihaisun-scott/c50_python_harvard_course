
# vertical columns
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end = "")

main()

# horizonal 
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# print matrix
def main():
    print_square(3)

def print_square(size):
    for i in range(size): # for each row
        for ii in range(size): # for each col
            print("#", end = "") # add brick
        print() # new line

def print_square(size):
    for i in range(size): # for each row
        print("#" * size)
    print()
    
main()


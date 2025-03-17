try: 
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")



# different version of above
while True: # keeps going until an integer is given
    try: 
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")
    # else: # can also break here
    #     break
        
print(f"x is {x}")



# improving upon this
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: # keeps going until an integer is given
        try: 
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else: # can also break here
            break
    return x

main()

# using pass to stay in the loop
# improving upon this
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True: # keeps going until an integer is given
        try: 
            return int(input(prompt))
        except ValueError:
            pass # staying in the loop "pass = ignore"

main()
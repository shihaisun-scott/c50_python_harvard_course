

def main():
    x = int(input("What's x? "))

    if is_even(x): # remainder
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
    # cleaner versions
    # return True if n % 2 == 0 else False 
    # return n % 2 == 0
    
main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s.isalnum(): # no punct, spaces, etc
        return False
    
    if not (2 <= len(s) <= 6): # min 2 chars and max 6
        return False
    
    if not s[:2].isalpha(): # must start with two letters
        return False
    
    # get idx and number of first number
    ifirst = len(s)
    first = None
    for i,letter in enumerate(s):
        if letter.isnumeric():
            ifirst = i
            first = letter
            break
    
    if first == "0": # first char cannot be a number
        return False
    if first is not None and not s[ifirst:].isnumeric(): # first to last need to be numbers
        return False 
    
                
    return True # passed all tests
            

if __name__ == "__main__":
    main()  
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    # get idx and number of first number
    ifirst = len(s)
    first = []
    for i,letter in enumerate(s):
        if letter.isnumeric():
            ifirst = i
            first = letter
            break
    if not s[:2].isnumeric(): # must start with two letters
        if 2 <= len(s) <= 6: # min 2 chars and max 6
            if first != "0": # first number cannot be 0
                if s[ifirst:].isnumeric(): # numbers must be at the end
                    if s.isalnum(): # no periods, spaces, or punct
                        return True
                
    return False
            


main()
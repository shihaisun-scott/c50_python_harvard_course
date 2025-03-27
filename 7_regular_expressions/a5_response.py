from validator_collection import validators, checkers, errors

def main():
    print(valid_email(input("What's your email address?: ")))
    

def valid_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()
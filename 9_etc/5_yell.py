
def main():
    yell(["This", "is", "CS50"])

##  example 1
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

## example 2
# map: apply a function to each of the values
def yell(*words):
    uppercased = map(str.upper, words) # each value in words will be uppercased
    print(*uppercased)

## example 3
# list comprehensions: generate a list with logic
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()



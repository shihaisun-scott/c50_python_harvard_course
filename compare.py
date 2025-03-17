x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: # boolian expression: true or false answer
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y: # can also use else
    print("x is equal to y")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
# ask user for their name
name = input("What's your name? ")

# using the strip function to remove whitespaces (left and right side)
name = name.strip()

# can also capitalize
name = name.capitalize()

# capitalize all words instead of just the first letter
name = name.title()

# do all
name = name.strip().title()

# say hello to user
print("hello,", name) # print by default adds space for each argument

print("hello, ", end = "") # the default end is to start a new line
print(name)

print(f"hello, {name}") # another way to solve the same problem

# printing out a quote
print("hello, 'friend'")
print("hello, \"friend\"") # backslash to escape

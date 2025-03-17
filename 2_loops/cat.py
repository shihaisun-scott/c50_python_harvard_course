
# while loop
i = 0
while i < 3:
    print("meow")
    i += 1

# for loops
for i in [0, 1, 2]:
    print("meow")

# better for loops
for _ in range(3): # range is up to but not through
    print("meow")

# another version
print("meow\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n > 0: # break out when the user gives a pos value
        break

for _ in range(n):
    print("meow")
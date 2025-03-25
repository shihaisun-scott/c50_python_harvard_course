with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstip()) # need to remove the line added in the end


# a better version than above, but cannot sort (cannot iterate and sort):
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


# get list of names first and then you can edit it
names = [] # assign first
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
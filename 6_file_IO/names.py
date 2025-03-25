# rm text.txt to remove the file

name = input("What's your name? ")
with open("names.txt", "a") as file: # a to append; w to write (overwrites)
    file.write(f"{name}\n") # file automatically close using with

# file.close() # using with is better
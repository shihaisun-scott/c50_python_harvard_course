# command in-line example using sys and sys,arg
import sys

# check for errors
if len(sys.argv) < 2: # two because 0 is the program and 1 is the input (len == 2)
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1]) 


# another version of above
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") # exit early to prevent the error later on
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") # 
print("hello, my name is", sys.argv[1]) 


# slicing
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") # exit early to prevent the error later on

for arg in sys.argv[1:]:
    print("hello my name is", arg)
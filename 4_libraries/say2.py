import sys

from sayings import hello # import only one of the functions in sayings

if len(sys.argv) == 2:
    hello(sys.argv[1])

# note that main will always be called whenever the file is loaded, even if only hello is imported
# use if __name__ == "__main__" to prevent this 
# count the number of lines in a code
# exclude comments and blanks

import sys

def main():
    if len(sys.argv) != 2:
        print("Use one argument")
        sys.exit()

    if sys.argv[1].endswith(".py"):
        count = 0
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.strip()
                    if not line.startswith("#") and not line == "":
                        count += 1 ## gcheck if line of code is blank or comment
        except FileNotFoundError:
            print("File not found")
            sys.exit()
    else:
        print("File does not end with .py")
        sys.exit()

    print(f"{sys.argv[1]} has {count} lines")

if __name__ == "__main__":
    main()
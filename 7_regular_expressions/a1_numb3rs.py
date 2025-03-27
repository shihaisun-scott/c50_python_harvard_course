# ip address needs to be #.#.#.# and each # between 0-255 inclusive

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for num in matches.groups():
            if not 0 <= int(num) <= 255:
                return False
        return True # passed the tests in the loop
    else: 
        return False


if __name__ == "__main__":
    main()
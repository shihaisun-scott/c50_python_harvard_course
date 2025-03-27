# count all "um" from string
import re
import sys

# um
# um?
# Um, thanks for the album
# Um, thanks, um

def main():
    print(count(input("Text: ")))


def count(s):
    # if matches := re.search(r"(\bum\b)", s.strip(), re.IGNORECASE): # note that search only searches the first instance
    if matches := re.findall(r"\bum\b", s.strip(), re.IGNORECASE):
        n = len(matches) 
    else:
        n = 0
    return n


...


if __name__ == "__main__":
    main()
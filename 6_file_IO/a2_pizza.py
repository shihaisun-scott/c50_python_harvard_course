import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Use only one arg")
    
    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        with open(file_name) as file:
            menu = csv.DictReader(file)
            print(tabulate(menu, headers = "keys", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
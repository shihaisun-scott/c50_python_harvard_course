# input argument of csv to read and csv to save

import sys
import csv

def main():

    if len(sys.argv) != 3:
        sys.exit("Input two arguments")

    filename = sys.argv[1]
    savename = sys.argv[2]

    if not filename.endswith(".csv") or not savename.endswith(".csv"):
        sys.exit("Both files must be csv")

    try:
        with open(filename, "r") as file, open(savename, "w", newline="") as outfile:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(outfile, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                house = row["house"]
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
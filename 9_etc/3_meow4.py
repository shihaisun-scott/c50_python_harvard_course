import argparse

parser = argparse.ArgumentParser(description="Meows like a cat")
parser.add_argument("-n", help="number of times to meow", type=int) # make int for me
args = parser.parse_args()

# do "meows.py -h" to get help

for _ in range(args.n):
    print("meow")
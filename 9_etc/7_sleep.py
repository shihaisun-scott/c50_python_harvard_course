# generate

def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep" * n)
    return flock

if __name__ == "__main__":
    main()

# printing too many sheep will not work because the computer cannot handle it
# use generators
# yield -- tell python to return one value at a time; generating a little piece of data at a time
def sheep(n):
    for i in range(n):
        yield("sheep" * i)
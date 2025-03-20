import random

def main():
    level = get_level("Level: ")
    n = random.randrange(level) + 1

    guess = get_guess("Guess: ", n)

    print("Just right!")


def get_level(prompt):
    while True:
        level = input(prompt)
        if level.isnumeric():
            level = int(level)
            if level > 0:
                return level
        
def get_guess(prompt, n):
    while True:
        guess = int(input(prompt))
        while guess != n:
            if guess > n:
                print("Too large!")
            elif 0 < guess < n:
                print("Too small!")
            guess = int(input("Guess: "))
        break

if __name__ == "__main__":
    main()

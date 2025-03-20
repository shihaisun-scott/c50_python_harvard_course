import random

def main():
    level = get_level("Level: ")

    count_correct = 0
    count_wrong = 0
    for iquestion in range(10):
        if count_wrong < 3:
            num1 = generate_integer(level)
            num2 = generate_integer(level)

            guess = input(f"{num1} + {num2} = ")
            if check_int(guess):
                if int(guess) == num1 + num2:
                    count_correct = count_correct + 1
                else:
                    count_wrong = count_wrong + 1
                    print("EEE")
            else:
                print("EEE")
                
    print(f"Score = {count_correct} out of 10")

def get_level(prompt):
    while True:
        level = input(prompt)
        if check_int(level):
            if int(level) in [1, 2, 3]:
                return int(level)

def generate_integer(level):
    if level == 1:
        return random.randrange(1,10)
    elif level == 2:
        return random.randrange(11,100)
    elif level == 3:
        return random.randrange(101, 1000)
    
def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
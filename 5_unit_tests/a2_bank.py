def main():
    prompt = input("Greeting: ")
    print(value(prompt))


def value(prompt):
    prompt = prompt.lower().strip()
    if prompt[:5] == "hello":
        return "$0"
    elif prompt[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
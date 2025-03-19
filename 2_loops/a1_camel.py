# convert camel text(thisText) to snake text (this_text)
def main():
    camel = input("camelCase: ")
    snake = ""
    for letter in camel:
        if letter.isupper():
            letter = "_" + letter.lower()
        snake = snake + letter
    print(snake)

if __name__ == "__main__":
    main()
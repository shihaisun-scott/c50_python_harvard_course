def main():
    text = input("Input: ")
    print(convert(text))

def convert(text):
    vowel = ["a","e","i","o","u"]
    for letter in text:
        if letter.lower() in vowel:
            text = text.replace(letter,"")
    return text

if __name__ == "__main__":
    main()
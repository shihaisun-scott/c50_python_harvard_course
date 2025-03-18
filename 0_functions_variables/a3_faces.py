# turning :) and :( into emojis

def main():
    prompt = input("Insert prompt: ")
    print(convert(prompt))

def convert(text):
    return text.replace(":)", "\U0001F642").replace(":(", "\U00002639")

main()
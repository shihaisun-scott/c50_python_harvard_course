import inflect

def main():
    text = say_adieu("Name: ")
    print(text)

def say_adieu(prompt):
    names = []
    p = inflect.engine()
    while True:
        try:
            name = input(prompt)
            names.append(name)
        except EOFError:
            return f"Adieu, adieu, to {p.join(names)}"
        
if __name__ == "__main__":
    main()

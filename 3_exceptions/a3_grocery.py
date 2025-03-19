def main():
    grocery = {} # empty list
    while True:
        try:
            item = input("").strip().upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            grocery_ordered = sorted(grocery)
            for item in grocery_ordered:
                print(f"{grocery[item]} {item}")
            break

main()
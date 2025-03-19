def main():
    coins = [25, 10, 5]
    due = 50
    while due > 0:
        print(f"Amount Due: {due}")
        insert = int(input("Insert Coin: "))
        if insert in coins:
            due = due - insert
    print(f"Change owed: {due*-1}")

if __name__ == "__main__":
    main()
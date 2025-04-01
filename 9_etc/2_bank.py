# global variables

balance = 0

def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposit(n):
    global balance # inform the function that balance is a global variable
    balane += n

def withdraw(n):
    global balance
    balane -= n

if __name__ == "__main__":
    main()

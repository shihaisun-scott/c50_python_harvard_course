def main():
    x,y,z = str.split(input("Expression: "))
    if y == "+":
        print(float(x) + float(z))
    if y == "-":
        print(float(x) - float(z))
    if y == "/":
        print(float(x) / float(z))
    if y == "*":
        print(float (x) * float(z))
    
if __name__ == "__main__":
    main()
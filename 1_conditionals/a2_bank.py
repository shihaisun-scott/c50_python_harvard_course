def main():
    prompt = input("Greeting: ").lower().strip()
    if prompt[:5] == "hello":
        print("$0")
    elif prompt[0] == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
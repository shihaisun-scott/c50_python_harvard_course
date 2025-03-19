def main():
    file = input("File name: ").split(".")
    extension = file[-1]
    if extension in ["gif", "jpg", "jpeg", "png"]:
        print(f"image/{extension}")
    elif extension in ["pdf", "zip"]:
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
    else:
        print("none")

if __name__ == "__main__":
    main()
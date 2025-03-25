import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Needs three argyments: .py image image")

    infile = sys.argv[1]
    outfile = sys.argv[2]
    shirt = Image.open("shirt.png")

    if not infile.endswith((".jpg", ".jpeg", ".png")) or not outfile.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Both files need to be jpg, jpeg or png")

    if infile.split(".")[-1] != outfile.split(".")[-1]:
        sys.exit("Both files need to have the same extension")

    try:
        image = Image.open(infile) # open 
        image = ImageOps.fit(image, shirt.size) # resize and crop with ImageOps.fit
        image.paste(shirt, (0, 0), shirt) # overlay the shirt with Image.paste
        image.save(outfile) # save the result with Image.save
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
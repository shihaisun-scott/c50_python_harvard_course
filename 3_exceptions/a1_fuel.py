def main():
    x = convert("Fraction: ")
    if x < 1:
        print("E")
    elif x > 99:
        print("F")
    else:
        print(f"{x}%")

# define convert
def convert(prompt):
    while True: # keep going until a fraction is given
        try: 
            xy = input(prompt).split("/")
            perc = int(int(xy[0]) / int(xy[1]) * 100)
            if perc > 100:
                continue # go again
            return perc
        except (ValueError, ZeroDivisionError):
            pass

main()




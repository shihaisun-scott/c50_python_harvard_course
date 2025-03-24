def main():
    perc = convert(input("Fraction: "))
    print(gauge(perc))
    

# define convert
def convert(prompt):
    while True: # keep going until a fraction is given
        try: 
            xy = prompt.split("/")
            perc = int(int(xy[0]) / int(xy[1]) * 100)
            if perc > 100:
                continue # go again
            return perc
        except (ValueError, ZeroDivisionError):
            pass


def gauge(perc):
    if perc < 1:
        return "E"
    elif perc > 99:
        return "F"
    else:
        return f"{perc}%"


if __name__ == "__main__":
    main()
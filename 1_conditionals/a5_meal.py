def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")


def convert(time): # convert the 24hr time into a float
    time = time.split(":")
    return float(time[0]) + float(time[1])/60


if __name__ == "__main__":
    main()
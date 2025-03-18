
def main():
    cost = input("How much was the meal? ")
    tip_perc = input("What percentage would you like to tip? ")
    tip = tip_calc(cost, tip_perc)
    print(f"Leave ${tip:.2f}")

def tip_calc(cost, tip_perc):
    # remove the $ and % first
     cost = float(cost.removeprefix("$"))
     tip_perc = float(tip_perc.removesuffix("%"))
     return cost * tip_perc / 100

main()
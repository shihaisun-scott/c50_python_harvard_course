import requests
import sys
import json

def main():
    # check if a value is set
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit()

    # check if the value is a float
    n = get_n()

    # get bitcoin price
    bs_usd = get_bitcoin()

    # output n bitcoins to USD. use , as thousand separator
    price = bs_usd * n
    print(f"${price:,.2f}")


# sysarg needs to be float and length of 2
def get_n():
    try: 
        n = float(sys.argv[1])
        return n
    except ValueError:
        print("Command-line argument not a number")
        sys.exit()


def get_bitcoin():
    try: 
        bitcoin = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        bitcoin = bitcoin.json()
        bc_usd = float(bitcoin["data"]["priceUsd"])
        return bc_usd
    except requests.RequestException:
        sys.exit()


if __name__ == "__main__":
    main()
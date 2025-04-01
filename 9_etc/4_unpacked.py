# unpacking: unpacking a list of multiple values

# example 1
first, last = input("What's your name? ").split("")
print(f"hello, {first}")


# example 2
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]
# print(total(*coins), "knuts") # the * unpacks

# can also do this with dict
coins = {
    "galleons": 100,
    "sickles": 50,
    "knuts": 25
}

print(total(**coins), "knuts") # the ** unpacks


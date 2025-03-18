# importing libraries

import random
# can also load specific functions from the library
#   from random import choice

# random choice
coin = random.choice(["heads", "tails"])
print(coin)

# random integer
number = random.randint(1, 10)
print(number)

# shuffling the list
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


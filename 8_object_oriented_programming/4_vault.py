
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self): # to print the result
        return f"{self.galleons} G, {self.sickles} S, {self.knuts} K"
    
    def __add__(self, other): # operator overloading
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 0, 100)
print(weasley)

total = potter + weasley
print(total)


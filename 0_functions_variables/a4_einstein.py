# e = mc sq

def main():
    mass = int(input("Enter mass in kg: "))
    print("Energy =", energy(mass), "Joules")

def energy(mass):
    c = int(3 * pow(10,8))
    return int(mass * pow(c,2))

main()
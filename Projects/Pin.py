import random
digits = "1234567890"
length = 4
pin = ""

for a in range(length):
    pin+=random.choice(digits)


print("Your four digit pin is ready!", pin)
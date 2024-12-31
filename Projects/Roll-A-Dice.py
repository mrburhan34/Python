import random


while True:
    choice = input("Roll a dice? (y/n): ").lower()
    if choice == "y":
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print(f"({d1}, {d2})")
    elif choice == "n":
        print("Thanks for choosing us!")
        break
    else:
        print("Invalid Choice")
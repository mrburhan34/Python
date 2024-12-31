import random as ran

digits = ("1234567890")
leng = 12
accNo = ""

for a in range(leng):
    accNo+= ran.choice(digits)


def payment(Bill, accountNo, pin, accNo, Bank_Balance):
    while True:
        yourBill = int(input(f"Amount You wanna transfer from {accNo}: "))
        if yourBill == Bill:
            askPin = int(input("Enter Your Pin: "))
            if askPin > 999 and askPin < 10000:
                askMe = int(input(f"Enter Pin of {accountNo}: "))
                if askMe == pin:
                    Bank_Balance+=yourBill
                    print("Payment Successful!")
                    print(f"Your Bank Balance is {Bank_Balance}")
                    break
                else:
                    print("Incorrect Pin!")
            else:
                print("Incorrect Pin!")
        else:
            print("Incorrect Bill!")

def menu():
    print("1. Osmania   - 5RS")
    print("2. Tea       - 10RS")
    print("3. Coffee    - 15RS")
    print("4. Noodles   - 20RS")
    print("5. Pasta     - 20RS")

def takeOrder():
    accountNo = 500013428134
    pin = 1340
    cost = {1: 5, 2: 10, 3: 15, 4: 20, 5: 20}
    while True:
        try:
            askOrder = int(input("What do you wanna order? "))
            if askOrder in cost:
                x = int(input("How many? "))
                print("Here's your Order, Enjoy your food!")
                Bill = (cost[askOrder] * x)
                askBill = input("Do you want bill? ").lower()
                if askBill == "yes":
                    print(f"Your Bill is: {Bill}RS")
                    payment(Bill, accountNo, pin, accNo, Bank_Balance)
                    break
                elif askBill == "no":
                    print("Okay!")
                else:
                    print("Invalid Input! Please answer 'yes' or 'no'.")
            else:
                print("Invalid menu choice! Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("-----Welcome To Mrburhan34's Cafe-----")
while True:
    Bank_Balance = 0;
    askMenu = input("Do you want the menu? (y/n/q): ").lower()

    if askMenu == "y":
        menu()
        takeOrder()
    elif askMenu == "n":
        takeOrder()
    elif askMenu == "q":
        break
    else:
        print("Sorry, I didn't get you. Please answer 'yes' or 'no'.")

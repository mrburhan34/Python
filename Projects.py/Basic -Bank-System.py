Balance = 1000

print("----WELCOME TO MY APP----")
print("    Your Initial Balance Is 1000")
def menu():
    print("")
    print("    1. Check Total Balance: ")
    print("    2. Withdraw Money")
    print("    3. Deposit Money")
    print("    4. Quit")

while True:

    menu()
    choice = int(input("How may I help you: "))
    if (choice == 1):
        print("Your current balance is", Balance)
        print("")
    elif (choice == 2):
        withdraw = float(input("Enter amount you want to withdraw: "))
        if (Balance >= withdraw > 0):
            Balance -= withdraw
            print("Your current balance is", Balance)
            print("")
        elif (Balance < withdraw or Balance == 0):
            print("Insufficient Money!")
            print("")
        elif (withdraw < 0):
            print("Invalid Input!")
            print("")
        else:
            print("Invalid Input!")
    elif (choice == 3):
        deposit = float(input("Enter amount you want to deposit: "))
        if (deposit < 0):
            print("Invalid Input!")
            print("")
        elif (deposit > 0):
            Balance += deposit
            print("Your current balance is", Balance)
            print("")
    elif (choice == 4):
        print("Thanks For Using My App!")
        print("")
        break
    else:
        print("Invalid Input!")
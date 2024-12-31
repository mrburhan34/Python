def main():
    while True:
        num1 = int(input("Enter your first number: "))

        op = input("Enter your Arithmetic operator (+, -, *, /): ")

        num2 = int(input("Enter your second number: "))

        if(op == "+"):
            print(num1, "+", num2, "=", num1 + num2)

        elif(op == "-"):
            print(num1, "-", num2, "=", num1 - num2)

        elif(op == "*"):
            print(num1, "*", num2, "=", num1 * num2)

        elif(op == "/"):
            print(num1, "/", num2, "=", num1 / num2)

        else:
            print("Invalid Input!");

        ask = input("Do you wanna quit? ").upper()
        if(ask == "YES"):
            print("Thanks for using this game!")
            break

main()
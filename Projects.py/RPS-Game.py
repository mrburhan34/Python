import random

while True:
    print("\nLet's play Rock Paper Scissor!")
    print("Rock")
    print("Paper")
    print("Scissor")
    print("Shoot!")

    Player1 = input("Choose yours: ")
    Player1 = Player1.upper()

    options = ["ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER", "SCISSOR","ROCK", "PAPER"]
    Player2 = random.choice(options)

    print("You: ", Player1)
    print("Computer: ", Player2)

    if Player1 == Player2:
        print("It's a draw!")
    elif Player1 == "ROCK" and Player2 == "PAPER":
        print("COMPUTER WON!")
    elif Player1 == "PAPER" and Player2 == "ROCK":
        print("YOU WON!")
    elif Player1 == "PAPER" and Player2 == "SCISSOR":
        print("COMPUTER WON!")
    elif Player1 == "SCISSOR" and Player2 == "PAPER":
        print("YOU WON!")
    elif Player1 == "SCISSOR" and Player2 == "ROCK":
        print("COMPUTER WON!")
    elif Player1 == "ROCK" and Player2 == "SCISSOR":
        print("YOU WON!")
    else:
        print("Invalid Input!")

    quit = input("Do you want to quit? (yes to exit, no to play again): ").lower()
    if quit == "yes":
        print("Thanks for playing!")
        break

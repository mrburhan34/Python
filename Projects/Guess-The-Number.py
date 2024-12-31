import random

Number = random.randint(0,100)

while True:
    guess = int(input("Guess the Number between 1 to 100: "))
    if guess == Number:
        print("Congrats! You are correct...")
        break
    elif guess > Number :
        print("Too High!!")
    elif guess < Number:
        print("Too Low!!")
    else:
        print("Please Enter Valid Number.")
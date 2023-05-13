import random

# guessing game

def guess(x):
    random_number = random.randint(1,x)
    print(f"{random_number}")
    guess =0
    while guess != random_number:
        User_guess =int(input(f"guess a number between 1 and {x}: "))
        if User_guess > random_number:
            print("Sorry ,guess again. Too high")
        elif User_guess < random_number:
            print("Sorry ,guess again. Too low")

    print(f"correst guess {random_number}")


guess(10)                   


def computer_guess(x):
    low=1
    high=x
    feedback =" "
    while feedback !="c" and low != high :
        if low != high:
            guess =random.randint(low,high)
        else :
             guess =low 

        feedback = input(f"Is {guess} too high (H),too Low (L) , or correct (C) ??").lower
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":   
            low = guess + 1 

    print(f"correst guess {guess}")   
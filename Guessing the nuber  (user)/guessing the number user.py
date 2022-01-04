import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f" Guess number between 1 and {random_number}: "))
        if guess > random_number:
            print("Too high try again")
        elif guess < random_number:
            print("Too low try again")
    print(f"Yee you found the number {random_number} correctly")


def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = str(input(f"is {guess} too high (H), too low(L) or correct(C)"))
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
    print(f"yaay the computer guessed your number {guess} correctly")
        
computer_guess(20);
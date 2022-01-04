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

        
guess(20);
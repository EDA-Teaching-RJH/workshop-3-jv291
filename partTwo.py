import random
secret_number= random.randint(1, 10)
guess = int(input("Pick a number between 1 and 10:"))
if guess == secret_number:
    print("correct")
elif guess > secret_number:
    print("too high")
elif guess < secret_number:
    print("to low")

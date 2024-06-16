import random


def get_int(prompt):
    while True:
        temp = input(prompt)
        if not temp.isnumeric():
            print("Please enter an integer number")
        else:
            return temp


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(get_int(": "))

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    elif guess <= answer:
            print("Please guess higher")
    else:
        print("Please guess lower")
        
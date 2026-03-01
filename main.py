import random

secret_number = random.randint(1, 100)

print("I am thinking of a secret number between 1 and 100")

#Ask the player to guess this number 5 times
for i in range(1, 6):
    print("Take a guess")

    guess = int(input('>'))

    if guess > secret_number:
        print("Your guess is too high")
    elif guess < secret_number:
        print("Your guess is too low")
    else:
        break


if guess == secret_number:
    print("Good job!!! You guessed the number")
else:
    print('Nope! the number was {}'.format(secret_number))


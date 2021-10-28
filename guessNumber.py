import random

rand = random.randint(1, 100)
guess = 0

while True:
    print("Enter a number to guess or a word to quit")
    try:
        guess = int(input())
    except ValueError:
        break
    if guess == rand:
        print("You got the number")
        break
    else if guess < rand:
        print("Too low")
    else if guess > rand:
        print("Too high")
        
print("Thanks for guessing, the correct number was:", str(rand))

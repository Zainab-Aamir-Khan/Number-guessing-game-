#number guessing game 
import random

print("welcome To The Number Guessing Game!!!")
guessNumber = random.randint(1,100)


while True:
    try:
        guess = int(input("enter any number to guess: "))

        if guess < guessNumber:
            print("The number is too low!")
        elif guess > guessNumber:
            print("The number is too high!")
        else:
            print("YAHOO! you guessed right!")
            break
    except:
        print("Sorry boss! you entered wrong number!")
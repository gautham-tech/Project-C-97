import random

print("Number Guessing Game")
print("Enter a number between 1 and 9")
r1 = random.randint(1, 9)
chances=5
while (1): 
    guess = int(input("Enter your guess:"))
    chances=chances-1
    if guess<r1:
        print("Guess a number greater than",guess)
    elif guess==r1:
        print("CONGRATULATIONS YOU WON!!")
        break
    else:
        print("Guess a number lesser than ",guess)
    if chances==0 :
        print("Your chances are over! YOU LOSE!!")
        break
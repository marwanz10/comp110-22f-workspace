"""An example of condintiona (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("You get bitches")
else:
    print("Sorry, incorrect you get no fucking bitches :(")
    print( "Also you a fucking BITCH!!!")
    if guess > SECRET:
        print("You guessed to high!")
    else:
        print("You gussed too low!")

print("Game over.")
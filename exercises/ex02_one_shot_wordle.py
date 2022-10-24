"""EX02 - One-shot Wordle - Loops!"""

__author__ = "935081174"
secret_word = "python"

guess: str = input("What is your 6-letter guess?: ")
word_length: int = 6
i = 0
output: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while word_length != len(guess):
    guess = input("That was not 6 letters! Try again: ")
if guess == secret_word:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")
else:
    while i < len(secret_word):
        if guess[i] == secret_word[i]:
            output = output + GREEN_BOX
        else:
            if (secret_word.__contains__(guess[i])):
                True
                output = output + YELLOW_BOX
            else:
                output = output + WHITE_BOX
        i = i + 1
    print("Not quite. Play again soon! ")
    print(output)
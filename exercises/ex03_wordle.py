"""EX03 - Structured Wordle!"""

__author__ = "935081174"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_through: str, single_character: str) -> bool:
    """Returns whether or not the single character is found in the seached word."""
    assert len(single_character) == 1
    if (searched_through.__contains__(single_character)):
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Codeifies guess."""
    i = 0
    output: str = ""
    assert len(guess) == len(secret)
    while i < len(secret):
        if contains_char(secret, guess[i]) is True:
            if guess[i] == secret[i]:
                output = output + GREEN_BOX
            else:
                output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
        i = i + 1
    return output


def input_guess(expected_length: int) -> str:
    """Correct # of characters."""
    guess: str = input("Enter a " + str(expected_length) + " character word: ")
    while expected_length != len(guess):
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    i = 0
    number_of_turns = 1
    while i < 6:
        print("=== Turn " + str(number_of_turns) + "/6 ===")
        number_guess = input_guess(len(secret))
        print(emojified(number_guess, secret))
        if secret == number_guess:
            print("You won in " + str(number_of_turns) + "/6 turns! ")
            i = 7
        i = i + 1
        number_of_turns += 1
    if i < 7:
        print(" X/6 - Sorry, try again tomorrow!")

    
if __name__ == "__main__":
    main()

"""EX06 - Choose Your Own Adventure!"""

__author__ = "935081174"
import random
COWBOY: str = "\U0001F920"

points: int = 0
player: str = ""
character: str = ""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    greet()
    print(f"lets get started! {COWBOY}")
    question_list: list[str] = [question1, question2, question3, question4]
    for q in random.sample(question_list, k=4):
        answer: int = q()
        global points
        points += answer
        if points > 50:
            quit(f"Ok, have a great day. Danger Level: {points - 100 }")
    if points < 15:
        points += question5()
    else:
        points += question6()
    say_my_name(points)
    print(f"And your person is.... {character}!!!! Danger level: { points } ")
    play_again: str = input("Would you like to play again (respond yes or no) ")
    if play_again == ("yes"):
        points = 0
        main()
    else:
        print(f"Thank you for playing, {player}! ")
       
        
def greet() -> None:
    """Greeting and welcome message."""
    global player
    player = input("What is your name? ")
    print(f"Welcome { player }, Today you are going to figure out which Breaking Bad character you are!")
    return None
   

def question1() -> int:
    """Get Danger level from question 1."""
    print("There is a threat against you. What's your response?")
    print("1. Drown yourself in the pool.")
    print("2. Change your identity.")
    print("3. Lay low.")
    print("4. Punch your problems away.") 
    print("5. Run over them.") 
    print("6. Blow them up.") 
    print("7. Plan your vengeance in silence.")
    print("8. Eat breakfast.") 
    print("9. End Game.")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question1()
    answer_choice = int(answer_choice)
    if answer_choice >= 10 or answer_choice < 1:
        print("That was not a choice. Please try again ")
        return question1()
    if answer_choice == 9:
        answer_choice = 100
    return int(answer_choice)
    

def question2() -> int:
    """Get Danger level from question 2."""
    print("Do you like children? ")
    print("1. I love kids. ")
    print("2. I love my children. ")
    print("3. I like children as long as they're well behaved ")
    print("4. If you can pay me, I'll tolerate them.")
    print("5. End game.")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question2()
    answer_choice = int(answer_choice)
    if answer_choice >= 6 or answer_choice < 1:
        print("That was not a choice. Please try again")
        return question2()
    if answer_choice == 5:
        answer_choice = 100
    return int(answer_choice)


def question3() -> int:
    """Get Danger level from question 3."""
    print("On a scale of 1-9, how evil are you? ")
    print("1. There isn't a bad bone in your body. ")
    print("2. You're too sutpid to be evil. ")
    print("3. You're a good person, capable of doing bad things. ")
    print("4. You've done terrible things, but you know right from wrong. ")
    print("5. You used to think you were a good person, now you're not so sure. ")
    print("6. Like everything, your moral have a price. ")
    print("7. You'd pretend to drown a small boy to teach his brother a lesson .")
    print("8. You'd slit someone's throat to teach people a lesson. ")
    print("9. You are the danger. ")
    print("10. End Game. ")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question3()
    answer_choice = int(answer_choice)
    if answer_choice >= 11 or answer_choice < 1:
        print("That was not a choice. Please try again ")
        return question3()
    if answer_choice == 10:
        answer_choice = 100
    return int(answer_choice)


def question4() -> int:
    """Get Danger level from question 4."""
    print("How would you describe yourself ")
    print("1. Anxious ")
    print("2. Practicial ")
    print("3. Witty ")
    print("4. Calm ")
    print("5. End Game.")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question4()
    answer_choice = int(answer_choice)
    if answer_choice >= 6 or answer_choice < 1:
        print("That was not a choice. Please try again ")
        return question4()
    if answer_choice == 5:
        answer_choice = 100
    return int(answer_choice)


def question5() -> int:
    """Get Danger level from question 5."""
    print("How smart are you ")
    print("1. I know what I need to know")
    print("2. I'm well rounded.")
    print("3. People underestimate my intelligence.")
    print("4. I'm a genius")
    print("5. End Game.")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question5()
    answer_choice = int(answer_choice)
    if answer_choice >= 6 or answer_choice < 1:
        print("That was not a choice. Please try again ")
        return question5()
    if answer_choice == 5:
        answer_choice = 100
    return int(answer_choice)


def question6() -> int:
    """Get Danger level from quesiton 6."""
    print("Describe your general temper ")
    print("1. Patient ")
    print("2. It usually takes a lot to get me angry ")
    print("3. It can be explosive when someone tries to take advantage of me ")
    print("4. I have my moments ")
    print("5. End Game.")
    answer_choice: str = input("(answer as a number): ")
    if answer_choice.isdigit() is False:
        print("That was not an answer choice. Please try again. ")
        return question6()
    answer_choice = int(answer_choice)
    if answer_choice >= 6 or answer_choice < 1:
        print("That was not a choice. Please try again ")
        return question6()
    if answer_choice == 5:
        answer_choice = 100
    return int(answer_choice)


def say_my_name(dangerlevel: int) -> None:
    """Find out which character you are based off Danger level."""
    global character
    if dangerlevel == 6 or dangerlevel == 7:
        character = "Skylar White "
    if dangerlevel == 8 or dangerlevel == 9:
        character = "Hank Schrader "
    if dangerlevel == 10 or dangerlevel == 11:
        character = "Jesse Pinkman "
    if dangerlevel == 12 or dangerlevel == 13:
        character = "Mike Ehrmantraut "
    if dangerlevel == 14 or dangerlevel == 15:
        character = "Saul Goodman "
    if dangerlevel == 16 or dangerlevel == 17:
        character = "Tuco Salamanca "
    if dangerlevel == 18 or dangerlevel == 19:
        character = "Lydia Rodarte-Quayle "
    if dangerlevel == 20 or dangerlevel == 21:
        character = "Gustavo Fring "
    if dangerlevel == 22 or dangerlevel == 23:
        character = "Jack Welker "
    if dangerlevel >= 24:
        character = "Walter White "
    return None
    
    
if __name__ == "__main__":
    main()
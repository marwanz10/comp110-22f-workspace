"""EX01 - Chardle - A cute step toward Worldle."""

__author__ = "935081174"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters ")
else:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Character must be a single character.")
    else:
        print("Searching for " + letter +  "in " + word)
        if letter == word [0] :
            print ( letter + "found at index 0 " )
        if letter == word [1] :
            print ( letter + "found at index 1 " )
        if letter == word [2] :
            print ( letter + "found at index 2 " )
        if letter == word [3] :
            print ( letter + "found at index 3 " )
        if letter == word [4] :
            print ( letter + "found at index 4 " )
        
        my_counter = word.count(letter)
        if my_counter == 0:
            print("No instances of " + letter + "found in " + word)
        else:
            if my_counter == 1:
             print ("1 instance of " + letter + " found in " + word)
        
            else:
                print (str(my_counter ) + "instances of " + letter + "found in " + word )
            


        
    
    
    





 




    


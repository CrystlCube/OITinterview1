import random

def printRules(userStatement): # Prints the rules for Hangman if the user requested them
    if userStatement.lower() == "rules" or userStatement.lower() == "\"rules\"":
        print("The goal of Hangman is guess a hidden word, which is displayed as a row of blanks that is as long as the word is. " + 
            "You can guess this word by choosing one letter at a time. If the letter is in the word, it replaces the blanks in each spot that the letter appears" + 
            "If not, it is displayed off to the side. \n The game ends when all of the letters in the word are guessed. " + 
            "This variation of the game is not case sensitive and also displays the length of the word next to the blanks as well.")
        print()
        print()
        return True
    return False

def printToString(list1): # Prints a list of [x,y,z] to a format of x y z (3)
    for i in list1:
        print(i, end=" ")
    print("(" + str(len(list1)) + ")", end = "")
    print()

# Open the word bank
try:
    f = open("wordBank.txt", "r")
    wordBank = f.read().split("\n")
except:
    wordBank = ["mouse", "engineer", "cougars", "aspen", "soybean", "elephant", "pneumonia", "telescoping", "chlorophyll", "syzygy"]


# Introduction to the game
print("Welcome to the game of Hangman! If you'd like to read the rules or access them at any point during the game, type \"rules\" then press Enter. If you're ready, go ahead and press Enter!")
userStart = input()
printRules(userStart)

while True: # Start of each new game, new word is selected
    trueWord = random.choice(wordBank)
    wordLen = len(trueWord)
    guessedCorrect = []
    guessedIncorrect = []
    wordGuess = ['_' for i in range(wordLen)]
    count = 0

    print("Here is your word.")
    printToString(wordGuess)
    while True: # Run for each letter
        while True: # Checking input
            userInput = input("Enter the letter you'd like to guess for the word: ")
            print()
            if printRules(userInput):
                continue

            if len(userInput) != 1 or not userInput.isalpha(): # Check to make sure input is only one letter
                print("That is not a valid letter choice. Try again!")
                continue
            userChar = userInput[0].lower() # Check to make sure input hasn't been guessed yet
            if userChar in guessedCorrect or userChar in guessedIncorrect:
                print("You already guessed this letter. Try entering a letter you haven't tried yet!")
                continue
            break
        
        # Check to see where in the word the letter is (if at all)
        count += 1
        inWord = False
        for i in range(wordLen):
            if userChar == trueWord[i]:
                wordGuess[i] = userChar
                inWord = True

        if inWord:
            print("Your letter " + userChar + " was in the word!")
            guessedCorrect.append(userChar)
        else:
            print("Your letter " + userChar + " wasn't in the word. Try another letter!")
            guessedIncorrect.append(userChar)

        # Display current guesses and progress
        print("Here are your guesses so far.")
        print()
        printToString(wordGuess)
        print()
        print("Incorrect guesses: ", end="")
        printToString(guessedIncorrect)
        print("Correct guesses: ", end="")
        printToString(guessedCorrect)
        print("Total guesses: " + str(count))
        print()
        print()
    
        # Check to see if the player has solved the word
        if '_' not in wordGuess:
            print("Congratulations, you solved the word! You used " + str(count) + " total guesses and only " + str(len(guessedIncorrect)) + " incorrect guess" + ("." if len(guessedIncorrect) == 1 else "es."))
            break

    # Check to see if the user would like to play again
    print("Would you like to play again? If you'd like to quit, type \"quit\" then press Enter. Otherwise, type anything then press Enter.")
    userAgain = input()
    if userAgain.lower() == "quit" or userAgain.lower() == "\"quit\"":
        print("Thanks for playing!")
        break
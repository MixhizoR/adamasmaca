def main():
    print("This is hangman game!")
    print("You are starting with selecting a word to other's guess")
    print("If you cannot guess the word in 8 tries, you lose")
    print("You can only enter a letter or guess the full word")
    while True:
        guessedLetters = []
        guesses = 8
        word = input("Enter the word: ").lower()
        if not word.replace(' ','').isalpha():
            print("Please enter a word")
            continue
        while(guesses > 0):
            printWord(word, guessedLetters)
            print(f"Guessed letters are: {guessedLetters}")
            print(f"You have {guesses} guesses left")
            guessedLetter = input("Guess a letter: ").lower()
            if guessedLetter == word:
                printWord(word, guessedLetters)
                print("Congrats! You won.")
                print(f"The word is: {word}")
                break
            elif len(guessedLetter) > 1 or not guessedLetter.isalpha():
                print("Please enter a letter")
            elif guessedLetter in guessedLetters:
                print("Please enter a word that has not been entered")
            else:
                guessedLetters.append(guessedLetter)
                if guessedLetter in word:
                    print("Nice one!")
                else:
                    guesses -= 1
                    if guesses == 0:
                        print("You Lose :(")
                        print(f"The word was: {word}")
                    else:
                        print("Ooops!")
            if isSublist(word,guessedLetters):
                printWord(word, guessedLetters)
                print("Congrats! You won.")
                print(f"The word is: {word}")
                break

def printWord(word, guessedLetters):
    for i in range(50):
        print()
    for letter in word:
        if letter == " ":
            print("")
        elif letter in guessedLetters:
            print (letter)
        else:
            print("-")

def isSublist(a,b):
    for i in a:
        if i == " ":
            continue
        elif i not in b:
            return False
    return True

if __name__ == "__main__":
    main()
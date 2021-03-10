# MIT 6.0001 PS 2
# Hangman Game
# By Shaurya Goyal

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word_is_guessed = True
        else:
            word_is_guessed= False
            break
    return word_is_guessed


def get_guessed_word(secret_word, letters_guessed):
    word_guessed = ""
    word_guessed_list = []
    for i in range(len(secret_word)):
        word_guessed_list+= "1"
        word_guessed_list[i] = "_ "
    for b in range(len(secret_word)):   
        for a in range(len(letters_guessed)):
            if letters_guessed[a] == secret_word[b]:
                word_guessed_list[b] = letters_guessed[a]
    for char in word_guessed_list:
        word_guessed += char
    return word_guessed

def get_available_letters(letters_guessed):
    available_letters_list=[]
    available_letters = ""
    for i in range(len(string.ascii_lowercase)):
        available_letters_list += string.ascii_lowercase[i]
    
    for e in letters_guessed:
        available_letters_list.remove(e)      
    
    for alpha in range(len(available_letters_list)):
        available_letters += available_letters_list[alpha]
    return available_letters

def hangman(secret_word):
    print("\nWelcome to the game Hangman !.\n \nRules: \n1. You will get 6 guesses. \n2. You will lose one guess for each incorrect consonant and lose 2 guesses for each incorrect vowel. You do not lose a guess for a correct alphabet. \n3. You will also get 3 warnings in cases you repeat an alphabet already guessed or enter a character that in not an alphabet and so on. Once you run out of warnings, you will lose a guess for any such entry. \n4. Enter only one alphabet at once")
    print("\n \nThe game has started.")
    print("\n \nI am thinking of a word that is", len(secret_word), "letters long. \n \nYou have 6 guesses remaining. \n \nYou have 3 warnings remaining.\nAvailable letters:", string.ascii_lowercase)
    warnings = 3
    guess_remaining = 6
    word_is_guessed = False
    letters_guessed = []
    while guess_remaining > 0:
        if word_is_guessed == False:
            guess = input("Please guess an alphabet:")       
            if guess in string.ascii_lowercase :
                if guess not in letters_guessed:
                    letters_guessed += guess
                    if guess in secret_word :
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! That letter in not in the word", get_guessed_word(secret_word, letters_guessed))
                        if guess in "aeiou":
                            guess_remaining-=2
                        else:
                            guess_remaining-=1
                else:
                    print("\nYou have already guessed this alphabet.")
                    if warnings >0:
                        warnings-=1
                        print("You have",warnings,"warnings left")
                    else:
                        guess_remaining-=1
                        print("No warnings left.  You lose a guess.")
            else:
                print("\nThis is not an alphabet.")
                if warnings >0:
                    warnings-=1
                    print("You have",warnings,"warnings left")
                else:
                    guess_remaining-=1
                    print("No warnings left.  You lose a guess.")
            
                
            word_is_guessed = is_word_guessed(secret_word, letters_guessed)
            if word_is_guessed == True:
                print("Congratulationsn you have won the game ! \nYour score is", guess_remaining*len(secret_word))
                break
            
            if guess_remaining >0:
                print("Available letters:", get_available_letters(letters_guessed))
                print("You have", guess_remaining, "guesses remaining.")
            else:
                break

                
    if guess_remaining<=0:
        print("\nYour guesses are over. You have lost the game. The word was", secret_word)


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

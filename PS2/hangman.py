# MIT 6.0001 PS 2
# Hangman Game
# By Shaurya Goyal

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():

    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word_is_guessed = True
        else:
            word_is_guessed= False
            break
    return word_is_guessed

def match_with_gaps(my_word, other_word, letters_guessed):

    
    letters_guessed1 = []
    letters_guessed2=""
    for char in letters_guessed:
        letters_guessed2 += char

    for char in my_word:
        
        if char.isalpha():
            letters_guessed1.append(char)
        
    if len(my_word.strip()) != len(other_word.strip()):
        return False
    
    for i in range(len(my_word)):
        current_letter =  my_word[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = current_letter == other_letter
            if not has_same_letter:
                return False
            
        else:
            if current_letter == '_' and other_letter in letters_guessed1:
                return False
        if current_letter =="_":
            if other_letter in letters_guessed2:
                return False
        
    return True

def show_possible_matches(my_word, letters_guessed):

    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word, letters_guessed):
            matched_words.append(word)
    
    if len(matched_words) > 0:
        for word in matched_words:
            print(word, end=' ')
        print()
    else:
        print('No matches found')


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
    print("\nWelcome to the game Hangman !\n \nRules: \n1. You will get 6 guesses. \n2. You will lose one guess for each incorrect consonant and lose 2 guesses for each incorrect vowel. You do not lose a guess for a correct alphabet. \n3. You will also get 3 warnings in cases you repeat an alphabet already guessed or enter a character that in not an alphabet and so on. Once you run out of warnings, you will lose a guess for any such entry. \n4. Enter only one alphabet at once. \n5. Enter the special character * (Shift + 8) to show the list of possible words. You do not lost a guess or warning when you use a hint. You need to succesfully guess at least one letter to use hints.\n6. Type pass to give up.")
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
            elif guess == "*":
              
                my_word=""
                eligibility=""
                my_word_list = []
                for i in range(len(secret_word)):
                    my_word_list+= "_"
                for b in range(len(secret_word)):   
                    for a in range(len(letters_guessed)):
                        if letters_guessed[a] == secret_word[b]:
                            my_word_list[b] = letters_guessed[a]
                for char in my_word_list:
                    my_word += char
                for alpha in my_word_list:
                    if alpha != "_":
                        eligibility += alpha
                
                if (len(secret_word) - len(eligibility)) < len(secret_word):
                    print(show_possible_matches(my_word, letters_guessed))
                else:
                    print("\nYou can only use a hint when you have succesfully guessed at least 1 letter !\n")
                    
            elif guess == "pass":
                print("You have lost the game. The word was", secret_word)
                break
                

                                 
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

if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)


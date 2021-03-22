# 6.0001 Problem Set 3

#
# Name          : Shaurya
# Time started  : 22nd March 2020 at 8:20 PM
# Time finished : 22nd March 2020 at 11:40 PM

import math
import random


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word, n):    #n = current hand length
    word=word.lower()
    score_part1=0
    score_part2=0
    for char in word:
        if char in "qwertyuioplkjhgfdsazxcvbnm":
            score_part1 += SCRABBLE_LETTER_VALUES[char]
    wordlen = len(word)
    score_part2=((7*wordlen)-(3*(n-wordlen))) 
    if score_part2 <1:
        score_part2 =1        
    word_score = score_part1*score_part2
    return word_score

def display_hand(hand):

    print ("Current hand:")
    for letter in hand.keys():
        for j in range(hand[letter]):
             print( letter, end=' ')   
                                 


def deal_hand(n):

    hand={}
    num_vowels = int(math.ceil(n / 3)) #ceil(n/3) means the smallest integer not less than n/3

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    vowels_in_hand = hand.keys()
    in_hand = ""
    for char in vowels_in_hand:
        in_hand += char
        
    p = random.choice(in_hand)
    hand[p] -= 1
    if hand[p] == 0:
        del hand[p]
    hand["*"] = 1
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand

def update_hand(hand, word):

    hand_clone = hand.copy()
    word = word.lower()
    for char in word:
        hand_clone[char] = hand_clone.get(char,0) - 1
    hand_clone2 = hand_clone.copy() #this clone is used to iterate over the dictionary hand_clone
    alphabet = hand_clone2.keys()   
    for i in alphabet:
        if hand_clone2[i] <=0:
            del(hand_clone[i])
    return hand_clone

def is_valid_word(word, hand, word_list):

    word=word.lower()
    hand_clone = hand.copy()
    for char in word:
        hand_clone[char] = hand_clone.get(char,0) - 1
        if hand_clone[char] < 0:
            return False
    for i in VOWELS:
        word1 = ""
        for t in word:
            if t != "*":
                word1 += t
            else:
                word1 += i
        if word1 in word_list:
            return True
    return False
    


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    t = 0
    hand_values = hand.values()
    for i in hand_values:
        t += i
    return t
    


def play_hand(hand, word_list):

    n = calculate_handlen(hand)
    total_score = 0
    updated_hand = hand.copy()
    while n > 0:
        print()
        display_hand(updated_hand)
        word = input('Enter word, or "!!" indicate you are finished:')
        if word != "!!":
            if is_valid_word(word, updated_hand, word_list) == True:
                points_earned = get_word_score(word, n)
                total_score += points_earned
                print(word, "earned", points_earned, "points. Total:",total_score)
            else:
                print("That is not a valid word. Please choose another word.")
            letters_in_hand = updated_hand.keys()
            letters_in_hand = list(letters_in_hand)
            for char in word:
                if char in letters_in_hand:
                    n -= 1
                    letters_in_hand.remove(char)     
            updated_hand = update_hand(updated_hand, word)
        else:
            print("Total score for this hand:", total_score)
            break
    if n<=0:
        print ("Ran out of letters. Total score for this hand:",total_score)
    return total_score


def substitute_hand(hand, letter):

    hand_tuple = hand.keys()
    hand_char = ""
    for char in hand_tuple:
        hand_char += char
    value = hand[letter]
    eligible = False
    while eligible == False:
        letter_swapped = random.choice("qwertyuiopasdfghjklzxcvbnm")
        if letter_swapped not in hand_char:
            del hand[letter]
            hand[letter_swapped] = value
            eligible = True
    return hand

 
def play_game(word_list):
    print("\nWelcome to the word game! \n\nRules: \n\n1.You will choose how many hands you want to play. \n\n2.You will be given a hand of letters and you make words using it. Irrespective of a correct word, you will use up the letters in your hand that you enter.There is no penalty enforced \n\n3.Before starting the game, you will asked if you want to swap a letter of your hand. PLease enter yes or no depending onyour preference. If you enter yes, the next question will ask you which letter you want to swap. You enter the letter you want to swap here. \n\n4.Once a hand is over, you will have the choice if you wish to replay that particular hand. \n\n5.After all ahnds are over, your final score will be displayed. \n\nEnjoy !")
    print("\n-----------------------------------------------------------")
    no_of_hands = int(input("Enter total number of hands:"))
    score5 = 0
    while no_of_hands > 0:
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        substituted_hand = hand.copy()
        satisfy = False
        while satisfy == False:
            swap = input("Would you like to swap a letter ?")
            swap = swap.lower()
            if swap == "yes":
                letter = input("Which letter would you like to swap ?")
                substituted_hand = substitute_hand(substituted_hand, letter)
                display_hand(substituted_hand)
            elif swap == "no":              
                satisfy = True
            else:
                print("Please enter yes or no !")
        repeat = True
        while repeat == True:
            handscore = play_hand(substituted_hand, word_list)
            imdone = input("Do you want to replay the hand ? ")
            imdone=imdone.lower()
            if imdone == "no":
                print()
                repeat = False
        score5 += handscore
        no_of_hands -= 1
    print("Total score over all hands is:", score5)
            

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    

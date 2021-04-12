
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    

    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):

        return self.message_text

    def get_valid_words(self):

        poop = self.valid_words.copy()
        return poop
                
    def build_transpose_dict(self, vowels_permutation):

        vowels_permutation = vowels_permutation.lower()
        vowels_permutation_upper = vowels_permutation.upper()
        transpose_dict ={'b': 'b', 'c': 'c', 'd': 'd', 'f': 'f', 'g': 'g', 'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'B': 'B', 'C': 'C', 'D': 'D', 'F': 'F', 'G': 'G', 'H': 'H', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
        for i in range(5):
            transpose_dict[VOWELS_LOWER[i]]=vowels_permutation[i]
            transpose_dict[VOWELS_UPPER[i]]=vowels_permutation_upper[i]

        return transpose_dict

    def apply_transpose(self, transpose_dict):

        enc_msg_list = []
        for char in self.message_text:
            if char in transpose_dict:
                beta = transpose_dict[char]
                enc_msg_list.append(beta)
            else:
                enc_msg_list.append(char)
        enc_message_string =""
        for t in enc_msg_list:
            enc_message_string+=t
        return enc_message_string
        
class EncryptedSubMessage(SubMessage):
    # def __init__(self, text):
    #     '''
    #     Initializes an EncryptedSubMessage object

    #     text (string): the encrypted message text

    #     An EncryptedSubMessage object inherits from SubMessage and has two attributes:
    #         self.message_text (string, determined by input text)
    #         self.valid_words (list, determined using helper function load_words)
    #     '''
    #     pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        possible_permutations = get_permutations("aeiou")
        n1=0
        for permutation in possible_permutations:
            enc_dict1 = message.build_transpose_dict(permutation)
            message_try = self.apply_transpose(enc_dict1)
            encr_msg_list = message_try.split()

            n=0
            for elem1 in encr_msg_list:
                if is_word(self.valid_words, elem1) == True:
                    n+=1
            
            if n > n1:
                n1 =n
                pala =""
                for words1 in encr_msg_list:
                    pala += words1 + " "
        return ( pala)


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.")
    permutation = "ouaei"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:\n", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    print("\nActual encryption:\n", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("\nDecrypted message:\n", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE

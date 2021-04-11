# Problem Set 4B
# Name: Shaurya
# Time Start: 11 march 4pm, 10.30 start
# break at 5 pm finish time is 1am
#time finish : 3.5 hours

import string


def load_words(file_name):


    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    return wordlist

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):

        return self.message_text

    def get_valid_words(self):

        word_copy = self.valid_words[:]
        return word_copy

    def build_shift_dict(self, bshift):

        alphabet_lower = string.ascii_lowercase
        alphabet_upper = string.ascii_uppercase
        alphabet_dict={}
        n=0
        for i in range(26):
            if i+bshift <= 25:
                alphabet_dict[alphabet_lower[i]] = alphabet_lower[i+bshift]
                alphabet_dict[alphabet_upper[i]] = alphabet_upper[i+bshift]
            else:
                alphabet_dict[alphabet_lower[i]]=alphabet_lower[n]
                alphabet_dict[alphabet_upper[i]]=alphabet_upper[n]
                n+=1       
        return alphabet_dict

    def apply_shift(self, shift):

        alphabet_dictio = self.build_shift_dict(self.get_shift())
        alphabet_keys= alphabet_dictio.keys()
        enc_msg_list = []
        for char in self.message_text:
            if char in alphabet_keys:
                beta = alphabet_dictio[char]
                enc_msg_list.append(beta)
            else:
                enc_msg_list.append(char)
        enc_message_string =""
        for t in enc_msg_list:
            enc_message_string+=t
        return enc_message_string


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.shift = int(shift)
        self.encryption_dict = self.build_shift_dict(self.get_shift())
        self.message_text_encrypted = self.apply_shift(self.get_shift())

        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return int(self.shift)

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''

        shifted_dict = self.build_shift_dict(self.get_shift())
        shifted_dict1 = shifted_dict.copy()
        return shifted_dict1
        

    def get_message_text_encrypted(self):

        return self.message_text_encrypted

    def change_shift(self, shift):

        self.shift = shift
        self.message_text_encrypted = self.apply_shift(self.get_shift())


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_list = load_words(WORDLIST_FILENAME)
        encr_msg_list = self.message_text.split()

        c=0
        n1=0
        pala =""
        for dec_key in range(1,27):
            attempt_dict = self.build_shift_dict(dec_key)
            givenlist1 = attempt_dict.values()
            givenlist=[]
            for owmwo in givenlist1:
                givenlist.append(owmwo)

            correctlist1 = attempt_dict.keys()
            correctlist =[]
            for wop in correctlist1:
                correctlist.append(wop)
            oompa =[]
            n=0
            for elem1 in encr_msg_list:
                word = ""
                for char in elem1:
                    if char in string.ascii_letters:
                        poop = givenlist.index(char)
                        poop1 = correctlist[poop]
                        word+= poop1
                    else:
                        word+= char
                oompa.append(word)
                if is_word(word_list, word) == True:
                    n+=1

            
            if n > n1:
                
                n1 =n
                c = dec_key 
                pala =""
                for words1 in oompa:
                    pala += words1 + " "
                
        return (26-c, pala)
            

            

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)

    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    ciper1= CiphertextMessage(get_story_string())
    print(ciper1.decrypt_message())






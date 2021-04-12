# Problem Set 4A
# Name: Shaurya
# Time Spent: 2 hours

def get_permutations(sequence):
    
    if type(sequence) != list:
        list1 = list(sequence)
    else:
        list1 = sequence[:]  
         
    if len(list1)==1:
        return list1
    else:
        listlen = len(list1)
        list_reduced=list1[:listlen-1]
        list2 = get_permutations(list_reduced)
        list3 = []
        for word in list2:
            for i in range(len(word)+1) :
                newword = "1"*(len(word)+1)
                new_word = list(newword)
                new_word[i] = list1[(listlen-1)]
                new_word[:i] = word[:i]
                new_word[i+1:] = word[i:]
                list3.append(new_word)
        list4 = []
        for word_list in list3:
            string = ""
            for alpha in word_list:
                string+= alpha
            list4.append(string)
        list5 = []
        for dup in list4:
            if not dup in list5:
                list5.append(dup)
        return list5
    


if __name__ == '__main__':
    example_input = input("Enter a word to find permutations:")
    example_input = example_input.lower()
    print('Input:', example_input)
    print('Actual Output:', get_permutations(example_input) )
    



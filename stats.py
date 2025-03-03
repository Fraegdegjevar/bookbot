def number_of_words(string):
    word_list = string.split()
    word_counts = {}
    
    for word in word_list:
        #.get looks for the key, and if not exist, initialises to
        # the default value (second argument to .get)
        word_counts[word] = word_counts.get(word, 0) + 1
    
    sum_words = len(word_list)
    
    return word_counts, sum_words

def char_count(string):
    char_list = list(string.lower())
    char_counts = {}
    
    for char in char_list:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    return char_counts

def sort_char_counts(char_counts):
    dict_list = []
    
    for char in char_counts:
        char_dict = {"character": char,
                     "count": char_counts[char]}
        dict_list.append(char_dict)
        
    dict_list.sort(reverse=True, key=lambda x: x["count"])
    
    return dict_list
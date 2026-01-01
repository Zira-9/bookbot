from collections import Counter

def get_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def character_count(file_contents):
    
    char_lower = file_contents.lower()
    char_dic= Counter(char_lower)

    return char_dic

def sort_dic(char_dic):
    new_sorted_dic = dict(sorted(char_dic.items(), key=lambda item: item[1], reverse = True))
    return new_sorted_dic
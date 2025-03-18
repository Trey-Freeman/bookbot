def sort_on(dict):
    return dict[1]

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_char_dict(dict):
    return sorted(dict.items(), key=sort_on, reverse=True)

def get_word_count(text):
    segmented_text = text.split()
    return len(segmented_text)

def get_char_count(text):
    char_dict = {
        'a': 0
    }
    lower_text = text.lower()
    for char in lower_text:
        if char in char_dict.keys():
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict.update({char: 1})

    return char_dict

def sort_dict(unsort_dict):
    sorted_by_values = dict(sorted(unsort_dict.items(), key=lambda item: item[1], reverse = True))
    return sorted_by_values
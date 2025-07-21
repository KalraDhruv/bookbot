def num_words_count(content):
    return len(content.split())

def occurence_by_character(content):
    new_dict = {}
    for character in content:
        character = character.lower()
        if character in new_dict:
            new_dict[character] += 1
        else: 
            new_dict[character] = 1
    return new_dict

def sorted_list(char_count_dict):
    def sort_index(char_count):
        return char_count["num"]
    char_count_list = []
    for key in char_count_dict:
        char_count_list.append({"char": key, "num":char_count_dict[key]})
    char_count_list.sort(reverse=True, key=sort_index)
    return char_count_list



import sys
from stats import num_words_count, occurence_by_character, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    return ""

def pretty_print(sorted_list, filepath, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    word_count = num_words_count(content)
    character_count_list = occurence_by_character(content)
    sorted_count_list = sorted_list(character_count_list)
    pretty_print(sorted_count_list,filepath,word_count)
    


main()


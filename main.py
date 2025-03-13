from stats import get_word_count, get_char_count, sort_dict
import sys

def get_book_text(path_to_file):
        try:
            with open(path_to_file) as f:
                book = f.read()
                return book
        except FileNotFoundError:
            print("Invalid path")


    
        
def main():
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book_path = sys.argv[1]
    #print(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    word_count = get_word_count(get_book_text(book_path))
    print(f"Found {word_count} total words")
    test_dict = get_char_count(get_book_text(book_path))
    print("--------- Character Count -------")
    #for key, value in test_dict.items():
    #    print(f"'{key}': {value}")
    test_dict_sort = sort_dict(test_dict)
    for key, value in test_dict_sort.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============ END ============")
    

main()
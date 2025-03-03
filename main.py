import sys
from stats import number_of_words, char_count, sort_char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    book_string = get_book_text(path_to_file=path_to_file)

    word_counts, total_words = number_of_words(book_string)
    
    char_counts = char_count(book_string)
    sorted_char_counts = sort_char_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_counts:
        if char_dict['character'].isalpha():
            print(f"{char_dict['character']}: {char_dict['count']}")
    print("============= END ===============")
            

main()

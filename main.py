import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    output = get_book_text(sys.argv[1])
    num_words = count_words(output)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    dict_chars = count_chars(output)
    dict_chars_sorted = sort_chars(dict_chars)
    print("--------- Character Count -------")
    for row in dict_chars_sorted:
        if row[0].isalpha():
            print(f"{row[0]}: {row[1]}")

    print("============= END ===============")
    
main()

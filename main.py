from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)
    num_words = num_of_words(book_text)
    num_char = character_count(book_text)
    sorted_report = sorted_char(num_char)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
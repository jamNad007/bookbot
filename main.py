from stats import count_words
from stats import countSortWords
from utils import get_book_text
import sys

# This script is the main entry point for the BookBot application.
# It takes a file path as an argument and performs various analyses on the book text.
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

if __name__ == "__main__":
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_path)} total words")
    print("--------- Character Count -------")
    countSortWords(book_path)
    print("============= END ===============")


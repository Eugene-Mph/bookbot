from stats import *
from report import *
import sys

try:
    book_path = sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        return content
    
    
def main():
    book = book_path.split("/")[-1]
    content = get_book_text(book_path)
    word_count = count_words(content)
    chars = count_char(content)
    print_report(book_path, word_count, chars)
    

if __name__ == "__main__":
    main()
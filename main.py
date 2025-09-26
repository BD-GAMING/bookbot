from stats import *
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        string = f.read()
        return(string)


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    
    book_text = get_book_text()
    words = book_text.split()
    count = len(words)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------")
    
    chtr_count = chr_count(book_text)
    for i, v in sorted(chtr_count.items(), key=short, reverse=True):
        if i.isalpha():
            print(f"{i}: {v}")
    print("============= END ===============")

main()
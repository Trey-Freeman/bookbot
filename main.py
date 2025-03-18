import sys
from stats import count_chars, count_words, sorted_char_dict

def main():
   if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   results = sorted_char_dict(count_chars(get_book_text(sys.argv[1])))
   print_analysis(sys.argv[1], count_words(get_book_text(sys.argv[1])), results)

def get_book_text(filepath):
    with open(filepath, 'r') as file:   
        return file.read()
    
def print_analysis(filepath, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count:
        print(f"{char}: {count}")
    print("============= END ===============")

main()
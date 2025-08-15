
from stats import get_word_count, get_frequencies, get_frequency_list
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_location = sys.argv[1]


def get_book_text():
    with open(book_location, "r") as f:
        return f.read()
    
def sort_frequencies(frequencies):
    return frequencies["count"]

words = get_book_text()

word_count = get_word_count(words)
frequencies = get_frequencies(words)
frequencies_list = get_frequency_list(words)
frequencies_list.sort( key=sort_frequencies, reverse=True)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_location}")

print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for freq in frequencies_list:
    print(f"{freq['word']}: {freq['count']}")

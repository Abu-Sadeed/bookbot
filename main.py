
from stats import get_word_count

def get_book_text():
    with open("books/frankenstein.txt", "r") as f:
        return f.read()

words = get_book_text()
print(f"{get_word_count(words)} words found in the document")
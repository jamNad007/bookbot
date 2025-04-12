from utils import get_book_text

# function to capture the total word count in a book
def count_words(text):
    book = get_book_text(text)
    words = book.split()
    word_count = len(words)
    return word_count

# function to capture the total character count in a book
def charactersCount(text):
    book = get_book_text(text)
    lower_case_text = book.lower()
    char_dict = {}
    for char in lower_case_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# function that counts alphabetic characters in a book, and sorts them in descending order
def countSortWords(text):
    text_dict = charactersCount(text)
    char_list = []

    for key in text_dict:
        if key.isalpha():
            char_list.append((key, text_dict[key]))
        else:
            continue
    char_list.sort(key=lambda x: x[1], reverse=True)
    
    for char in char_list:
        print(f"{char[0]}: {char[1]}")


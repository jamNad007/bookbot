# Function for loading a book from a file, and passing it's contents
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
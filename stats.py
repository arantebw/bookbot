def count_characters(book_text: str):
    letter_count = {}
    for letter in book_text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def count_words(book_text: str):
    return len(book_text.split())


def get_book_text(file_path: str):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

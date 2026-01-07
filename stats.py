def count_words(book_text: str):
    return len(book_text.split())


def get_book_text(file_path: str):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

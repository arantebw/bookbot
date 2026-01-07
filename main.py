def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


if __name__ == "__main__":
    main()

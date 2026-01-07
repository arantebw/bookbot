from stats import get_book_text, count_words


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")


if __name__ == "__main__":
    main()

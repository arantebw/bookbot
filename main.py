from stats import character_items, get_book_text, count_words, count_characters
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_file_path = sys.argv[1]
    print(f"Analyzing book found at {book_file_path}")

    print("----------- Word Count ----------")
    book_text = get_book_text(book_file_path)
    print(f"Found {count_words(book_text)} total words")

    print("--------- Character Count -------")
    characters_dict = count_characters(book_text)
    items = character_items(characters_dict)
    for i in items:
        print(f"{i['char']}: {i['num']}")


if __name__ == "__main__":
    main()

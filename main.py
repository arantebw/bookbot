from stats import character_items, get_book_text, count_words, count_characters


def main():
    print("============ BOOKBOT ============")
    book_file_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_file_path}")

    print("----------- Word Count ----------")
    book_text = get_book_text(book_file_path)
    print(f"Found {count_words(book_text)} total words")

    print("--------- Character Count -------")
    characters_dict = count_characters(book_text)
    items = character_items(characters_dict)
    for i in items:
        print(f"{i["char"]}: {i["num"]}")


if __name__ == "__main__":
    main()

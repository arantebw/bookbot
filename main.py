def count_letters(contents):
    letter_count = {}
    for letter in contents.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def count_words(contents):
    return len(contents.split())


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_letters(file_contents))


if __name__ == "__main__":
    main()

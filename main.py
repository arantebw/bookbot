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

    filename = "frankenstein.txt"
    print(f"**** Report of books/{filename} ****\n")

    print(f"{count_words(file_contents)} words found in the document\n")

    letters = count_letters(file_contents)
    letters_list = list(letters.items())
    letters_list.sort(key=lambda x: x[1], reverse=True)
    for item in letters_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print()

    print("**** End ****")


if __name__ == "__main__":
    main()

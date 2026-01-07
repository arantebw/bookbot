# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Features

- It reads the entire contents of a `.txt` file.
- It can count the total number of words of a file.
- It can count the number of characters of a file.

## How to use?

- Create a `books` directory.
- Save the sample `*.txt` file inside.
  - [frankenstein.txt](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt)
  - [mobydick.txt](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt)
  - [prideandprejudice.txt](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt)
- Then run the program.
  ```bash
  $ python main.py books/frankenstein.txt
  ```

## APIs

- `count_words(contents)`
- `count_characters(contents)`

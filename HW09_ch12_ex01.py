#!/usr/bin/env python
# HW09_ch12_ex01
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a
#     c
#     b
###############################################################################
# Imports

# Body
def most_frequent(s):
    letter_and_count = {}
    punctuation = " !.,"
    for letter in s:
        letter = letter.lower()
        if letter not in punctuation:
            letter_and_count.setdefault(letter, 0)
            letter_and_count[letter] += 1
    by_freq = []
    for x,y in zip(letter_and_count.keys(),letter_and_count.values()):
        by_freq.append((x,y))
    sorted_by_freq = sorted(by_freq, key=lambda x: x[1], reverse=True)
    for letter,count in sorted_by_freq:
        print(letter)

###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                  "sed do eiusmod tempor incididunt ut labore et dolore magna "
                  "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                  "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                  "uis aute irure dolor in reprehenderit in voluptate velit "
                  "esse cillum dolore eu fugiat nulla pariatur. Excepteur "
                  "sint occaecat cupidatat non proident, sunt in culpa qui "
                  "officia deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()

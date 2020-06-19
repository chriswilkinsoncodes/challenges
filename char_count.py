#! /usr/bin/env python3

# Create a function that returns a dictionary with keys representing the 
# characters in the string and values representing the frequency of each
# character in the string.

# As a validation check, also return the length of the string and the
# sum of the values in the dictionary. These values should be identical.

def char_count(str):
    freq = {}
    for char in set(str):
        freq[char] = str.count(char)
    return freq, len(str), sum(freq.values())

if __name__ == '__main__':
    str1 = 'Return the frequency of characters in this string.'
    print(char_count(str1))

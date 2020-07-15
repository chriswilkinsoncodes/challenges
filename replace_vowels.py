#!/usr/bin/env python3

'''
You are a record label marketing manager and have decided to jump on the
bandwagon of having artists replace a vowel in their name with an 'x'.

Not to be outdone, instead of replacing only one vowel, you've decided to
replace ALL the lowercase vowels!

Write a script to replace each vowel in a string with an 'x'.

Examples
replace_vowels('Ariana Grande') # output: 'Arxxnx Grxndx'
replace_vowels('Stevie Wonder') # output: 'Stxvxx Wxndxr'

Additional challenges:
* Replace uppercase vowels also.
* Get user input for the names to be converted and/or letters to be
  replaced/used for replacement. 
  for replacement.
* Assign different replacement values for different letters. 
  e.g. replace 'o' with 'x' and 'u' with 'v', etc.
'''

import re

def replace_vowels1(name):
    for letter in name:
        if letter in 'aeiou':
            name = name.replace(letter, 'x')
    return name

def replace_vowels2(name):
    for vowel in 'aeiou':
        name = name.replace(vowel, 'x')
    return name

def replace_vowels3(name):
    return ''.join('x' if letter in 'aeiou' else letter for letter in name)

def replace_vowels4(name):
    return name.translate(name.maketrans('aeiou', 'xxxxx'))

def replace_vowels5(name):
    return re.sub(r'[aouei]', 'x', name)


if __name__ == '__main__':
    print(replace_vowels1('Ariana Grande'))
    print(replace_vowels2('Stevie Wonder'))
    print(replace_vowels3('Ed Sheeran'))
    print(replace_vowels4('Aretha Franklin'))
    print(replace_vowels5('eden ahbez'))
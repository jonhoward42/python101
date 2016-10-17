#!/usr/bin/env python

## Strings stored in variables
variable1 = 'This is a string with single quotes'
variable2 = "This is a string with double quotes"
variable3 = "This string started with double quotes and contains text 'within single quotes'"
print(variable1)
print(variable2)
print(variable3)

## Escaping characters using "\"
print("This contains an apostrophie, doesn't it?")
print('This contains an apostrophie, doesn\'t it?')

## Dealing with legitimate "\" in a string
# print("c:\this\is\a\new\folder") # <- This will give loads of errors as characters are escaped and interpreted
print(r"c:\this\is\a\new\folder") # <- The "r" interprets the string, literally

## Manipulating variables
firstname = "Jon "
lastname = "Howard "
print(firstname + lastname)
print(firstname * 5)
print((firstname + lastname) * 5)

## Slicing up strings
variable4 = "My string"
print(variable4)
print(variable4[4]) # <- Print the 4th digit (starting from 0)
print(variable4[0]) # <- Print the leading digit (digit 0)
print(variable4[3:8]) # <- Print digits starting from 3 and finish when 8th is reached (3 to 7 basically)
print(variable4[:2]) # <- Print up to, and excluding, digit 2 (so 0 & 1)
print(variable4[3:]) # <- Print digit 3, onwards

## Determining the length of a string
variable5 = "Hello world"
print(variable5)
print(len(variable5))



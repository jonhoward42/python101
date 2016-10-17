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
lastname = "Howard"
print(firstname + lastname)
print(firstname * 5)
print((firstname + lastname) * 5)




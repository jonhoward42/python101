#!/usr/bin/env python

array = ['cheese', 'ham', 'tomato', 'mayo', 'baguette']

## A simple for loop, looping through all elements in a 1D array/list
print("Constituent ingredients:")
for output in array:
	print(output)

## As above but using a specific subset of array elements
print("Fillings:")
for output in array[0:4]:
	print(output)

## Introducing a "range" to a for loop
# Syntax for range is: range(<start>, <stop>, <step>)
# <start> and <step> are optional
for output in range(10): # <- Counts up from 0 in 10 iterations (so 0 to 9)
	print(output)

for output in range(5,10): # <- Counts from 5 up to the 10th digit after 0 (i.e. 5 to 9)
	print(output)

for output in range(0,10,2): # <- Countes up from 0 in 10 iterations in steps of 2 (so 0, 2, 4, 6, 8)
	print(output)

## Using a for loop and range to work through each element of an array
# This gives much the same result as the first loop above
for i in range(0, len(array)):
	print(array[i])

## Ten green bottles
for i in range(10, 0, -1):
        if i == 1:
                print('{0} green bottle hanging on the wall, {0} green bottle hanging on the wall.'.format(i))
                print('And if that 1 green bottle should accidentally fall, there\'d be no bottles hanging on the wall.')
        elif i == 2:
                print('{0} green bottles hanging on the wall, {0} green bottles hanging on the wall.'.format(i))
                print('And if 1 green bottle should to accidentall fall, there\'d be only {0} green bottle hanging on the wall.'.format(i - 1))
        else:
                print('{0} green bottles hanging on the wall, {0} green bottles hanging on the wall.'.format(i))
                print('And if 1 green bottle should to accidentall fall, there\'d be {0} green bottles hanging on the wall.'.format(i - 1))

## Display all multiples of 4 in a range of 0 to 100
for i in range(101):
	if (i % 4 == 0):
		print(i)

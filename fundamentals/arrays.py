#!/usr/bin/env python

## Create a 1D array variable (aka a list)
variable1 = ["one", "two", "three", "four", "five"]

## Display the nth element of an array
print(variable1[1]) # <- Print the first element
print(variable1[4]) # <- Print the 4th element

## Display the complete contents of a list
print(variable1)

## Temporarily append or process additional elements to a list
print(variable1 + ["six", "seven", "eight"])

## Append an additional element to an array
variable1.append("six")
print(variable1)

## Process elements of an array, in the same way as a string
print(variable1[:2]) # <- Print elements up to, and excluding, 2 (so 0 & 1)

## Manipulate elements of an array variable
variable1[1] = "won" # <- Modify element 1
print(variable1)
variable1[1:3] = ["too", "free"] # <- Modify elements 1 up to, but excluding, 3 (so 1 & 2)
print(variable1)

# Remove elements from an array
variable1[3:] = [] # <- Eliminate elements 3 onwards
print(variable1)
variable1[0:1] = [] # <- Eliminate elements from 0 up to, but excluding, 1 (so just 0)
print(variable1)
variable1[:] = [] # <- Eliminate all elements
print(variable1)


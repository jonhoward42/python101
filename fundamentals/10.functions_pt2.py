#!/usr/bin/env python

## A function with multiple undefined arguments

def add_numbers(*args):
	total = 0
	for value in args:
		total += value
	return total

print(add_numbers(1,4,8,16,32,48))
print(add_numbers(10,20,40))
print(add_numbers(42))

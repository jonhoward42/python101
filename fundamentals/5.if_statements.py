#!/usr/bin/env python

variable = 15

## Basic IF statement
if variable < 10: # <- Note the ":" symbol
	print("Less than 10!")

## Else IF (elif)
if variable > 16: # <- Greater than
	print("Greater that 16")
elif variable < 10: # <- Less than
	print("Less than 10")
elif variable == 15: # <- Equal to
	print("Number is 15")
elif variable != 14: # <- Not equal to
	print("Definitely not 14!")

## Else
temperature = 35
if temperature > 25:
	print("Time to put your shorts on")
else:
	print("It's not greater than 25C, best wear trousers")



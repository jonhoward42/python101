#!/usr/bin/env python

## Basic functions that print an output but return nothing
def startup():
	print("********************")
	print("** Startup screen **")
	print("********************")

def shutdown():
	print("*********************")
        print("** Shutdown screen **")
        print("*********************")

def currencyConvert(amount):
	rate = 1.5
	print('Converted amount is: {0}'.format(amount / rate))

## A function that performs some logic and returns a value
def idealGfAge(myAge):
	gfAge = (myAge / 2) + 7
	return gfAge

## A function that performance some logic, returns a value and assumes a default value if none is specified during the function call
def get_gender(sex = 'Unknown'): # <- Default value to assume if none is provided
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

startup()
currencyConvert(25)
print('My ideal GF age is: {0}'.format(idealGfAge(37)))
get_gender('m')
get_gender('f')
get_gender()
shutdown()


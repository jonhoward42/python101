#!/usr/bin/env python

## A basic while loop
counter=0
while counter < 10:
	print(counter)
	counter += 1

## Ten green bottles
i = 10
while i > 0: 
	if i == 1:
                print('{0} green bottle hanging on the wall, {0} green bottle hanging on the wall.'.format(i))
                print('And if that 1 green bottle should accidentally fall, there\'d be no green bottles hanging on the wall.')
        elif i == 2:
                print('{0} green bottles hanging on the wall, {0} green bottles hanging on the wall.'.format(i))
                print('And if 1 green bottle should to accidentall fall, there\'d be only {0} green bottle hanging on the wall.'.format(i - 1))
        else:
                print('{0} green bottles hanging on the wall, {0} green bottles hanging on the wall.'.format(i))
                print('And if 1 green bottle should to accidentall fall, there\'d be {0} green bottles hanging on the wall.'.format(i - 1))
	i -= 1

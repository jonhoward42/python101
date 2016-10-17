#!/usr/bin/env python

## Use the break command to break out of a loop
magicNumber=42
for n in range(101):
    if n is magicNumber:
        print('{0} is the magic number'.format(n))
        break
    else:
        print('{0} is NOT the magic number, perhaps {1} is?'.format(n, n+1))

## Use the continue command to bypass the rest of a loop and start the next loop iteration
# I don't think I've ever had to use similar in another language, but it might be useful
numbersTaken = [2, 5, 12, 13, 17]
print("Here are the numbers that are still available")
for n in range(1,20):
    if n in numbersTaken:
        continue # <- If the above condition is true, bypass the rest of the loop and start the next iteration
    print(n)

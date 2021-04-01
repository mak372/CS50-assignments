from cs50 import get_int
from sys import exit

while True:
    x = get_int("Height:")
    if x >= 1 or x <= 8:
        break

for i in range(x):
    for j in range(x):
        if i+j>= x-1:
            print("#",end="")
        else:
            print(" ",end="")
    print()
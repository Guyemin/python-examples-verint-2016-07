import sys 
import os

a = range (97,123)
b = range (97,123)
c = range (97,123)

letters = (range(97,123))
match = [chr(x)+chr(y)+chr(z) for x in letters for y in letters for z in letters]
print match
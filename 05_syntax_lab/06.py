from random import randint
index = 1
x = int(randint(1,10))
y = int(randint(1,10))
print "The X number is %s" % x
print "The Y number is %s" % y
while index != 0:
	if (index % x == 0):
		if (index % y == 0):
			print index 
			index = 0
			break
	index = index + 1

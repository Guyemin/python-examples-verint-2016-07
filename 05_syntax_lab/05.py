from random import randint
index = 1
x = randint(1,1000000)
while index != 0:
	index = index + 1
	if x % 7 == 0:
		if x % 13 == 0:
			if x % 15 == 0:
				print "Bingo!"
				print "This is the number: %s" % x
				index = 0
	x = randint(1,1000000)
	


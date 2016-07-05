from random import randint
index = 1
x = randint(1,100)
#print "The random number is %s" % x
while index != 0:
	print "Please guess the number"
	guess = int(raw_input())
	if x > guess: 
		print "Your number is lower"
		index = index + 1
	elif x < guess: 
		print "You number is higher"
		index = index + 1
	else:
		print "Bingo!"
		index == 0
		break
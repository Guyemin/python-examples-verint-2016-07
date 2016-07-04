from random import randint
sum = 0
for i in range (1,8):
	x = randint(0,100)
	print x
	sum = sum + x
print "The sum is %s" % sum
if sum % 7 == 0:
	print "Boom"
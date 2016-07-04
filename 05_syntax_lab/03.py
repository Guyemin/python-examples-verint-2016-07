from random import randint
sum = 0
x = randint(1,10000)
print "The number is %s" % x
while (x % 10) > 0:
	num = x % 10
	print num
	sum = sum + num
	x = x / 10
	
print "The sum is: %s" % sum
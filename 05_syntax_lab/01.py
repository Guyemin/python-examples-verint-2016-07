print "Please write 10 numbers"

high = int(raw_input())
for i in range (1,10):
	number = int(raw_input())
	if number > high:
		high = number
print "The highest number is:%s" % high
print "Please enter any word"
word = raw_input()
total = word
index = 0
while word != ' ':
	if index > 0:
		total = "%s %s"  % (word, total)
	print "Please add another word"
	word = raw_input()
	index = index + 1
print total

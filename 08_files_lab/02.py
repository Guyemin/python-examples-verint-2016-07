import sys

a= sys.argv[1]
b= sys.argv[2]
c= sys.argv[3]
with open (c, "w") as ccin:
	with open (a, "r") as aain:
		for line in aain:
			c = ccin.write(line)
		c = ccin.write("\n")
		with open (b, "r") as bbin:
			for line in bbin:
				c = ccin.write(line)
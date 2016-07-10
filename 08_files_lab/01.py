import sys
with open (sys.argv[1], "r") as fin:
	with open (sys.argv[2], "w") as fout:
		for line in fin:
			fout.write(line)

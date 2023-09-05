#!/usr/bin/python3
cons = 0
for i in range(122, 96, -1):
	print("{}".format(chr(i - cons)), end="")
	if cons == 0:
		cons = 32
	else:
		cons = 0

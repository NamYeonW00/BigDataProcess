#!usr/bin/python3

import sys

d = dict()

file = sys.argv[1]

with open(file, "rt") as fp:
	for line in fp:
		str_arr = line.split("::")
		genre_arr = str_arr[2].split("|")
		for g in genre_arr:
			if g.strip() not in d:
				d[g.strip()] = 1
			else:
				d[g.strip()] += 1

fp.close()

file = sys.argv[2]
with open(file, "wt") as fp:
	for k, v in d.items():
		data = "%s %d\n" % (k, v)
		fp.write(data)

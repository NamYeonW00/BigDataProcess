#!usr/bin/python3

import sys
import calendar

d = dict()
dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

file = sys.argv[1]

with open(file, "rt") as fp:
	for line in fp:
		str_arr = line.split(",")
		date = str_arr[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))

		rd = str_arr[0] + "," + dayofweek[day]
		if rd not in d:
			d[rd] = str_arr[2] + "," + str_arr[3]
		else:
			temp = d[rd].split(",")
			v = int(temp[0]) + int(str_arr[2])
			t = int(temp[1]) + int(str_arr[3])
			d[rd] = str(v) + "," + str(t)

fp.close()

file = sys.argv[2]
with open(file, "wt") as fp:
	for k, v in d.items():
		data = "%s %s\n" % (k, v)
		fp.write(data)

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']
total = []

row_id = 1
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		total.append(sum_v) 
	row_id += 1

total.reverse()

all = len(total)
num = all * 0.3
C = 'A'
i = 0
while i < len(total):
	if int(num - total.count(total[i])) >= 0:
		row_id = 2
		count = 0
		for row in ws:
			if total[i] == ws.cell(row_id, column = 7).value:
				ws.cell(row_id, column = 8).value = C
				num -= 1
				count += 1
			row_id += 1
		i += count
	elif C == 'A':
		num += all * 0.4
		C = 'B'
	else:
		break

while i < len(total):
	row_id = 2
	count = 0
	for row in ws:
		if total[i] == ws.cell(row_id, column = 7).value:
			ws.cell(row_id, column = 8).value = 'C'
			count += 1
		row_id += 1
	i += count

wb.save("student.xlsx")

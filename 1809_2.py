from pprint import pprint

field =[[1, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0]]

current_a = 0
current_b = 0

def change_field(a_incr, b_incr):
	try:
		global current_a, current_b, field
		field[current_a][current_b] = 0
		current_a += a_incr
		current_b += b_incr
		field[current_a][current_b] = 1
	except IndexError:
		print('Out of field!')
		return -1
	else:
		return 0

while True:
	pprint(field)
	move = input('Print direction (q for quit): ')
	if move == 'q':
		print('Game over!')
		break
	else:
		if move == 'd':
			result = change_field(1, 0)
		elif move == 'u':
			result = change_field(-1, 0)
		elif move == 'r':
			result = change_field(0, 1)
		elif move == 'l':
			result = change_field(0, -1)
		else:
			print('Please type d, u, r of l: ')
			continue
		if result == -1:
			print('Game over!')
		if field[3][7] == 1:
			print('*** WIN ***')
			pprint(field)
			break

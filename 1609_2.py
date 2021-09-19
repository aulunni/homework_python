d = {}

p = '+7-953-096-71-75'
def valide_number(p):
	if len(p) !=16:
		return False
	if p[0:3] != '+7-':
		return False
	if p[6] != '-' or p[10] != '-' or p[13] != '-':
		return False
	ap = p[3:6] + p[7:10] + p[11:13] + p[14:]
	digits = '0123456789'
	for sym in ap:
		if not sym in digits:
			return False
	return True
print(valide_number(p))

def add_to_book(name, phone):
	d[name] = phone
	return d
while True:
	name = input('Name: ')
	if name == 'q':
		print(d)
		break
	phone = input('Phone: ')
	if phone == 'q':
		print(d)
		break
	if valide_number(phone):
		print('Number is correct. Adding now')
		add_to_book(name, phone)
		print('New number added')
	else:
		print('Invalid number')

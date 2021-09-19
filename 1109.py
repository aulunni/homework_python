import string
# string module constants
import random

def create_str(width):
	return[random.choice(string.ascii_letters) for i in range(width)]
	s = ' '
	for el in l:
		s += el
	return s
#print(create_str(7))

def count_str(s):
	big = 0
	small = 0
	for sym in s:
		if sym.isupper():
			big+=1
		else:
			small+=1
	if big>small:
		return 1
	elif small>big:
		return 0
	else:
		return -1
s = create_str(8)
print(s)
#print(count_str(s))

def create_list_str(width,num):
	return[create_str(width) for i in range(num)]
	

def procent_str(width, num):
    l = [create_str(width) for i in range(num)]
    s = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        s += el
        s += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            s += '1'
        elif small > big:
            stats += 1
            s += '0'
        else:
            statr += 1
            s += '-1'
        
        s += ' '
    s += '> A ' + str(statb/(statb+stats+statr)*100) + '% '
    s += '> a ' + str(stats/(statb+stats+statr)*100) + '% '
    s += 'a == A ' + str(statr/(statb+stats+statr)*100) + '%'
    return s

print(procent_str(8, 8))

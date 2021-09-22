class Person():
	def __init__(self, name):
		self.name = name

class Student(Person):
	homework = 0
	knowledge = 0
	def get_knowledge(self):
		self.knowledge += 1
	def get_homework(self, n):
		self.homework += n
	def do_homework(self):
		if self.homework > 0:
			self.homework -=1
			knowledge = 1
		else:
			print('Ничего не делал!')

class Teacher(Person):
	work = 0
	def give_knowledge(self, *pupils):
		for pupil in pupils:
			pupil.get_knowledge()
			self.work+=1
	def give_homework(self, *pupils, n):
		for pupil in pupils:
			pupil.get_homework(n)
			work += 1

t = Teacher('A.A.')
import random
my_list = ['Sergey', 'Julia', 'Egor', 'Igor', 'Evelin', 'German', 'Bargat', 'Regina', 'Bogdan', 'Leonid', 'Xenia', 'Leonard', 'Ivan', 'Elena']
random.shuffle(my_list)
i = my_list.pop()
#p = Student(i)
#t.give_knowledge(p)
#print(p.knowledge)

class Rectangle():
	def __init__(self, w, h):
		self.w = w
		self.h = h
	def get_p(self):
		return(self.w+self.h)*2
	def get_s(self):
		return(self.w*self.h)
r = Rectangle(4,5)
r.get_p()
print(r.get_p())
r.get_s()
print(r.get_s())

import math
class Circle():
	def __init__(self, r):
		self.r = r
	def get_do(self):
		return(self.r*math.pi*2)
	def get_st(self):
		return(math.pi*self.r**2)
c = Circle(7)
c.get_do()
print(c.get_do())
c.get_st()
print(c.get_st())

class Triangle():
	def __init__(self, a, b, d, h):
		self.a = a
		self.b = b
		self.d = d
		self.h = h
	def get_prm(self):
		return(self.a+self.b+self.d)
	def get_ss(self):
		return(self.b*self.h/2)

tt = Triangle(4, 7, 8, 9)
tt.get_prm()
print(tt.get_prm())
tt.get_ss()
print(tt.get_ss())

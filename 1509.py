list_=[1,1,2,2]

set(list_)
#print(set(list_))

set_1={1,2,3,4,5,6}
set_2={4,5,6,7,8,9}

#print(set_1.isdisjoint(set_2))
#print(set_1 == set_2)
#print(set_1.issubset(set_2))
#print(set_1.issuperset(set_2))
#print(set_1.union(set_2))
#print(set_1.intersection(set_2))
#print(set_1.difference(set_2))

#print(set_1.symmetric_difference(set_2))
#print(set_1.update(set_2))
#print(set_1.intersection_update(set_2))
#print(set_1.difference_update(set_2))

#set_1.add(9)
#print(set_1)

#set_1.remove(9)
#print(set_1)

#set_1.pop()
#print(set_1)

#set_1.clear()
#print(set_1)

def unique_numbers(set_1):
	return list(set(set_1))
print(unique_numbers(set_1))

def intersection_lists(set_1, set_2):
	return list(set(set_1) & set(set_2))
print(intersection_lists(set_1, set_2))

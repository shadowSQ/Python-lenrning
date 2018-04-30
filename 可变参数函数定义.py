def cute(numbers):
	s = 0
	for num in numbers:	
		s = s+num*num
	return s
	
def cute2(*numbers):
	s = 0
	for num in numbers:	
		s = s+num*num
	return s
	
list1 = [2,3,4,5,2,1,2]

print("%d"% cute(list1))
print("%s"%cute2(*list1))


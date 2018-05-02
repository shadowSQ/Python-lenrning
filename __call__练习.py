#__call__方法练习
class Student(object):
	def __init__(self,name):
		self.name = name 
	def __call__(self,age):
		self.age = age
		print("My name is %s ."% self.name)
		print('My age is %s .'% self.age)
	    
s = Student('x')

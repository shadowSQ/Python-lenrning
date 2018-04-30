#类的创建

#_init_方法第一个参数永远是self，表示实例本身
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

bart = Student('Li',59)
print(bart.name)
		

def set_age(self,age):
	self.age = age

s = Student()	
	
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)	

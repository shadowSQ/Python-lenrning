#__iter__练习
'''
如果一个类想被用于for ... in循环，
类似list或tuple那样，
就必须实现一个__iter__()方法，
该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1	#初始化计数器	
	def __iter__(self):
		return self			#迭代对象为实例本身，返回自己
	def __next__(self):
		#这个式子注意理解，是同时进行的
		#下一次相加的数，第一个是self.b 
		#第二个是self.a+self.b
		#将他们分别给self.a 
		#self.b
		self.a,self.b = self.b,self.a+self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a
	#获取元素	
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a	
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
		#	if stop is None:
		#		stop = 0	
			a,b = 1,1
			L = []
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b = b,a+b
			return L
			
			
for n in Fib():
	print(n)
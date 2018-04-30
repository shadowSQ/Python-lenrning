
#filter 函数练习

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n != 0
	
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列	

# 打印1000以内的素数:
#for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break		

#回数

def _odd_iter1():
    n = 0
    while True:
        n = n + 1
        yield n

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
        
def pri():
    yield 1
    it = _odd_iter1()
    while True:
        n = next(it)
        yield n
        it = filter(is_palindrome,it)#这句话要去掉括号（n）！！巨坑
        
for n in pri():
    if n < 100:
        print(n)
    else:
        break		
        
        
    

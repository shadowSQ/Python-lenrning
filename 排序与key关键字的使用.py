L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def byname(t):
    return t[0]

def byscore(t):
    return -t[1]
#函数的作用是将L中的值一个一个传进来，
#然后得到返回值
print(sorted(L,key = byname))
print(sorted(L,key = byscore))

print(sorted(L,key = lambda t:t[0]))
print(sorted(L,key = lambda t:t[1]))
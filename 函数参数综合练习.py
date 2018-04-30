#综合练习
def f1(a, b, c=0, *args,city, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    if 'est1' in kw:
        print('est')

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
#f1(1,2)
#f1(1,2,c = 3)
#f1(1,2,3,'a','b')
#f1(1,2,3,'a','b',v=23)
f1(1,2,city='beijing',est=2)

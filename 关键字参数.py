def person(name,age,**kw):
    print('name:',name,'age',age,'other',kw)

person('li',45)
person('li',24,city='beijing',dizhi = 'quanhzou')

extra = {'sex':'nan','interest':'basketball'}

person('li',22,**extra)

#命令关键字
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
person('li',22,city = 'beijing',job = 'engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('li',25,'args',city = 'beijing',job = 'engineer')
    

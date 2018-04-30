d = {'a': 1, 'b': 2, 'c': 3}
for key in d.values():
    print(key)

print([i*i for i in range(1,100) if i%2==0])
print([m+n for m in 'ABC' for n in 'abc'])

import os
print([d for d in os.listdir('.')])

d = {'x':'a','b':'c'}
print([k+'='+v for k,v in d.items()])

L=['HEllo',18,'GADA']
print([s.lower() for s in L if isinstance(s,str)])

import functools
int2 = functools.partial(int,base=3)

print(int2('121'))

def triangles(max):
    n = 0
    L = [1]
    while n<max:
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        n = n+1
    return 'done'
for n in triangles(5):
    print(n)
    
L = [1,1]
print([L[i]+L[i+1] for i in range(len(L)-1)])

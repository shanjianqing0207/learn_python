def triangles():
    L = [1]
    while True:
        yield L
        L = [1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]
        
a = 0
for t in triangles():
    print(t)
    a = a+1
    if a == 10:
        break


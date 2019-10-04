def findMinAndMax(L):
    m1=m2=L[0]
    for a in L:
        while a>m1:
            m1 = a
    for b in L:
        while b<m2:
            m2 = b
    min = m2
    max = m1
    print(min,max)
 

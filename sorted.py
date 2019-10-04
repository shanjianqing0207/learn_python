L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
     for x in t:
         if isinstance(x,str):
             return x
     pass   
         
         

L2 = sorted(L, key=by_name)
print(L2)


def by_store(t):
    for p in t:
        if isinstance(p,int):
            return p
    pass


L1 = sorted(L,key=by_store)
print(L1)

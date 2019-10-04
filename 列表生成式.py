L1 = ['Hello', 'World', 18, 'Apple', None]
for x in L1:
    if isinstance(x, str) is False:
        L1.remove(x)
    else:
        x = x

L2 = [s.lower() for s in L1]

print(L2)



# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

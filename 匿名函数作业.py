L = list(filter(lambda x:x%2==1,range(1,20)))
print(L)


# 检验：
def is_odd(n):
    return n % 2 == 1

if L==list(filter(is_odd,range(1,20))):
    print('成功')
else:
    print('失败')

import math

def quadratic(a, b, c):
    if b*b-4*a*c < 0:
        return '无解'
    elif a == 0:
        return '也无解'
    else:
        x1 = (-b+math.sqrt(b*b-4*a*c))/2/a
        x2 = (-b-math.sqrt(b*b-4*a*c))/2/a
        return x1,x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

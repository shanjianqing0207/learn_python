from functools import reduce
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    lis=map(lambda x:DIGITS[x] ,[i for i in s if i!='.'])
    return reduce(lambda x,y:x*10+y,lis)/10**(len(s)-s.find(".")-1)
    


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

height = float(input('输入身高：'))
weight = float(input('输入体重：'))
BMI = float(weight/height/height)

if BMI >= 32:
    print('严重肥胖')
elif BMI >= 28:
    print('肥胖')
elif BMI >= 25:
    print('过重')
elif BMI >= 18.5:
    print('正常')
else:
    print('过轻')
    
   

    

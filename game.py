""" 用python设计的第一个游戏 """
temp = input("猜一下小王八在想哪个数字: ")
guess=int(temp)

if guess == 8:
    print("猜对了！你是王九蛋吗？")
else:
    print("猜错了！我心里想的是8，你是王七蛋吗？")

print("游戏结束，不玩了。")

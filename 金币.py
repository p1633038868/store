#
# import random
#
# num = random.randint(1,100)
# cion = 5000
# count = 0
# count = count + 1
# while True :
#      count = count + 1
#      cion = cion -150
#      a = input("prees you key word:")
#      a = int(a)
#      if a > num:
#         print("猜测大了，金币消耗150，剩余金币 " ,cion , "个")
#      elif a < num :
#         print("猜测小了，金币消耗150，剩余金币" , cion ,"个")
#      else:
#         cion = cion + 200
#         print("恭喜您猜对了,金币加成200，剩余金币" , cion ,"个")
#         break
#      if count >= 7:
#         print("次数已用光,游戏结束")
#         break
#      if cion <= 0 :
#         print("金币已经用完")
#         break
#


import random
num = random.randint(1,100)
print(num)
money = 5000
count = 0
while True :

    count = count + 1
    if money >= 0 :
        if count<=6:
            a = int(input("请输入数字："))
            if a == num :
                if count <= 3 :
                    money+=200
                    print(money)
                    print("恭喜你！猜对了！+200",count,"次")
                    break

            elif a > num :
                print("猜大了-200",count,"次")
                money = money - 200
                print(money)
            else :
                print("猜小了-200你猜了",count,"次")
                money = money - 200
                print(money)
        else:
            print("已近被锁",count,"次")
            break

    else :
        print("您没钱了",count,"次")
        break

print("答案为：",num)
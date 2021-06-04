# # 实现输入10个数字，并打印10个数的求和结果
n=1
sum=0
s=0
while n<=10:
     num = input("请输入10个数：")
     sum = int(sum) + int(num)
     n +=1
print()
print("10个数的和为:%d" % sum)
print("10个数的平均值为:%.2f" % (sum / 10))
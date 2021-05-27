deep = 20#井的深度20m
skip = 3#每次上爬3m
slide = 2#每次下滑2m
day = 0#计数的变量
while 1:#跳出来才结束的循环
    deep = deep-skip
    if deep < 0:
        break
    deep= deep+slide#往下滑
    day = day+1#天数逐渐加一
print("天数:",day)

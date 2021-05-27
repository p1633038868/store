
while True:
    a = int(input("输入三角形第一边长："))
    b = int(input("输入三角形第二边长："))
    c = int(input("输入三角形第三边长："))

    if a+b<c and a+c<b and b+c<a:
        print("三边不能构成三角形")
    elif a==b and a==c and b==c :
        print("等腰")
    elif a==b==c:
        print("构成等边三角形")
    elif a*a+b*b==c*c and a*a+c*c==b*b and b*b+c*c==a*a  :
        print("构成直角三角形")
    else:
        print("不能形成三角形")


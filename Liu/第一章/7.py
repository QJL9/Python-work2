import math
a=eval(input("第一个点的横坐标"))
b=eval(input("第二个点的横坐标"))
x=eval(input("第一个点的纵坐标"))
y=eval(input("第二个点的纵坐标"))
print("两点间距离为","{:.2f}".format(math.sqrt((a-b)**2+(x-y)**2)))
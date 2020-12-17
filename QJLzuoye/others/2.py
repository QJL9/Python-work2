a=c=eval(input("请输入一个整数："))     #输入整数，c只是用来保存
if a<0:                                #取绝对值
    a=-a
b=[]                                   #b用来存放各个位

while a!=0:                            #每次取一位数字加入b
    b.append(a%10)
    a=a//10
d=b.copy()                             #d是b的拷贝用来比较  
b.reverse()                            #reverse

for i in b:                            
    print(i)
if d==b:                               #如果b正序和倒叙相同，则b是回文数，否则不是
    print(f"{c}是回文数")
else:
    print(f"{c}不是回文数")

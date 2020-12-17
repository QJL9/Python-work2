s={'小李':[77,54,57],'小张':[89,66,78],'小陈':[90,93,80],'小杨':[69,58,93]}
def avg(a,b,c):
    return int((a+b+c)/3)
for i in s:
    print(i)
    s[i]=avg(s[i][0],s[i][1],s[i][2])
print(s)
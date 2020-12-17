s={'小李':[77,54],'小张':[89,66,78,99],'小陈':[90],'小杨':[69,58,93]}
def avg(list):
    return int(sum(list) / len(list))
for i in s:
    s[i] = avg(s[i])
print(s)

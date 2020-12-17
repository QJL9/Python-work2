def a85(dic):
    for i in dic:
        if dic[i][0]>=85 and dic[i][1]>=85 and dic[i][2]>=85:
            print('分数大于85的同学为：',i)

def asum(dic):
    for i in dic:
        print (i,'的成绩:')
        print(round(sum(dic[i]),2), end='\t')
        print(round(sum(dic[i])/len(dic[i]),2))

def a3(dic):
    l=list(dic.items())
    l.sort(key=lambda x:sum(x[1]))
    for i in l:
        print(i[0],end=' ')

dict={'01':[67,88,45],'02':[97,68,85],'03':[97,98,95],\
'04':[67,48,45],'05':[82,58,75],'06':[96,49,65]}

a85(dict)
asum(dict)
a3(dict)


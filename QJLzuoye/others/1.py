with open(r'D:\Bubble Sort.txt','r') as f:  #打开文件
    
    b=f.read()
    print(b)                              
    a=b.split(" ")                          #读取分词并转为列表
    print(a)
with open(r'D:\Bubble Sort.txt','a') as f:
    for i in range(len(a),1,-1):                #从后向前遍历列表
        for j in range(1,i):                    #遍历第二个到第i个
            if a[j-1]>a[j]:                     #若前一个元素大
                a[j-1],a[j]=a[j],a[j-1]         #则交换两者位置
        
        f.write("\n")                           #输出
        for i in a:            
            f.writelines(i)
            f.write(" ")                    
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser
import os
# from tkinter import colorchooser
root=tk.Tk()
# b=colorchooser.askcolor()
# #colorchooser.askcolor(initialcolor='#ff0000')
# print(b[0],b[1])
# root.mainloop()

# l = ttk.Label(root, text="Hello World", font="helvetica 24")
# l.grid(padx=10, pady=10)
# def getinputfile_btn1():
#     inputfilenamevar = filedialog.askopenfilename()
#     print(inputfilenamevar)

# def font_changed(font):
#     l['font'] = font
#     print(font)

# root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
# root.tk.call('tk', 'fontchooser', 'show')
# def getfont_btn7_(font):
#     global getfontvar
#     getfontvar = font
#     print(getfontvar)

# def getfont_btn7():
#     root.tk.call('tk', 'fontchooser', 'configure',
#     '-font', 'helvetica 24', '-command', root.register(getfont_btn7_))
#     root.tk.call('tk', 'fontchooser', 'show')

# btn7 = tk.Button(root,text="open...",command=getfont_btn7)
# btn7.grid()
# a = tk.IntVar()
# a.set(12.35)
# b=a.get()
# print(b)
def get():
    global text1
    print(type(text1.get('1.0', 'end').split("\n")),text1.get('1.0', 'end').strip().split("\n"))
btn1 = ttk.Button(root,text='get',command=get)
text1=tk.Text(root,width=25,height=20)
text1.insert('end -1 chars','asdasffwet')
text1.grid()

var1 = tk.StringVar()
var1.set('456')
print(type(int(var1.get())),var1.get())



btn1.grid()


root.mainloop()



    
# def wordfreq(path, text, topn):
#     jieba.add_word('马保国')
#     jieba.add_word('混元功法')
#     words = jieba.lcut(text.strip())
#     counts={}

#     f=open('马保国.txt', 'r')
#     text=f.read()
#     f.close()

#     stopwords=[line.strip() for line in open(path, 'r').readlines()]
#     for word in words:
#         if len(word)==1:
#             continue
#         elif word not in stopwords:
#             counts[word]=counts.get(word,0)+1
#     items=list(counts.items())
#     items.sort(key=lambda x :x[1], reverse=True)

#     f=open(path+'\\_词频.txt', 'w')
#     for i in range(topn):
#         word,count=items[i]
#         f.writelines("{}\t{}\n".format(word,count))
#     f.close()

# f=open('马保国.txt', 'r')
# text=f.read()
# f.close()
# wordfreq(r'C:\Users\QJL\Desktop', text, 300 )

# os.chdir("%CD%")
# wd = os.getcwd()
#print(os.path.expandvars('C:/Users/%USERNAME%/Desktop'))
# f=open('C:/Users/QJL/Desktop/123.txt','w')
# f.write('123')
# f.close()

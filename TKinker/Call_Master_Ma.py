import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence
from jieba import add_word, lcut
from os.path import expandvars
from wordcloud import WordCloud
from imageio import imread

# from time import sleep

root = tk.Tk()
root.title("Call_Master_Ma")
# root.geometry('522x650')
# varaibles

getwidthvar = tk.IntVar()
getwidthvar.set(100)

getheightvar = tk.StringVar()
getheightvar.set(100)
getmaxsizevar = tk.StringVar()
getminsizevar = tk.StringVar()
getwordnumvar = tk.StringVar()
getwordnumvar.set("50")

wordnumvar = tk.StringVar()
wordnumvar.set(200)


inputfilenamevar = tk.StringVar()
outputfiledirectoryvar = tk.StringVar()
outputfiledirectoryvar.set(expandvars("C:/Users/%USERNAME%/Desktop"))
maskfilenamevar = tk.StringVar()

choosecolorvar = tk.StringVar()
choosecolorvar.set('#130c0e')
getfontvar = tk.StringVar()


# functions
def getinputfile_btn1():
    global inputfilenamevar
    inputfilenamevar = filedialog.askopenfilename()
    evariable1 = inputfilenamevar()
    print(inputfilenamevar)


def getsavefile_btn2():
    global outputfiledirectoryvar
    outputfiledirectoryvar = filedialog.askdirectory()
    evariable2 = outputfiledirectoryvar
    print(outputfiledirectoryvar)


def getmaskfile_btn3():
    global maskfilenamevar
    maskfilenamevar = filedialog.askopenfilename()
    print(maskfilenamevar)


def getcolor_btn4():
    global choosecolorvar
    choosecolorvar = colorchooser.askcolor()
    print(choosecolorvar)


def getfont_btn7_(font):
    global getfontvar
    font = font.replace('{','')
    font = font.replace('}','')
    getfontvar = font.split()
    print(getfontvar,type(getfontvar))


def getfont_btn7():
    root.tk.call(
        "tk",
        "fontchooser",
        "configure",
        "-font",
        "helvetica 24",
        "-command",
        root.register(getfont_btn7_),
    )
    root.tk.call("tk", "fontchooser", "show")


def getwidth_label10(val):
    label10["text"] = int(float(val))


def getheight_label11(val):
    label11["text"] = int(float(val))


def getmax_label13(val):
    label13["text"] = int(float(val))


def getmin_label14(val):
    label14["text"] = int(float(val))


def getnum_label15(val):
    global getwordnumvar
    a = int(float(val))
    label15["text"] = a
    getwordnumvar.set(a)

    for i in range(int(float(val))):
        print(i)



def generate():
    
    items = []
    global inputfilenamevar
    global getwordnumvar
    global text1, text2, text3
    
    print("generating...")
    try:
        f = open(inputfilenamevar, "r")
    except IOError:
        pass  # //////////////////////message
    else:
        text = f.read()
        f.close()
        print("readsuccess")

    add_word("马保国")
    add_word("混元功法")
    for line in text3.get('1.0',"end").split("\n"):
        add_word(line)
        print(line)

    words = lcut(text.strip())
    counts = {}

    stopwords = [line.strip() for line in text2.get('1.0',"end").split("\n")]
    for word in words:
        #print(word)
        if len(word) == 1:
            continue
        elif word not in stopwords:
            counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print("analysesuccess")
    text1.delete('1.0',"end")
    for i in range(int(float(getwordnumvar.get()))):
        word, count = items[i]
        
        text1.insert("end -1 chars", "{}\t{}\n".format(word, count))
# try:
#     f=open(path+'\\_词频.txt', 'w')
# except IOError:
#     pass#////////////////////message
# else:
#     for i in range(topn):
#         word,count=items[i]
#         f.writelines("{}\t{}\n".format(word,count))
#     f.close()
# /////////////////////////


def startcall():
    global maskfilenamevar
    global choosecolorvar
    global getwordnumvar
    global getwidthvar
    global getheightvar
    global text1
    #global
    color=[0,0]
    color[1]= choosecolorvar[1]
    text = text1.get('1.0',"end")
    #text = [line.strip() for line in text1.get('1.0',"end").split("\n")]
    
    # try:
    #     mask = imread(maskfilenamevar.get())
    # except FileNotFoundError:
    #     pass            #///////////////////////
    if text=='':
        text='no words'

    wcloud=WordCloud(font_path=r'C:/Windows/Fonts/simhei.ttf',
    background_color = color[1],
    width=int(float(getwidthvar.get())),
    max_words=500,
    mask=None,
    height=int(float(getheightvar.get())),
    margin=2).generate(text)
    
    wcloud.to_file(outputfiledirectoryvar.get()+'/马保国41s65d1s5cloud.png')

    print("calling...")  # ////////////////////


# widgets

evariable1 = tk.StringVar()
evariable2 = tk.StringVar()
evariable3 = tk.StringVar()
#
mainfram = tk.Frame(root)
fram1 = ttk.Frame(mainfram, width=400, height=300, borderwidth=3)
# fram1_1=ttk.Frame(fram1,width=174,height=300,borderwidth=3)

fram2 = ttk.Frame(mainfram, width=200, height=300, borderwidth=3)
# fram2_1=ttk.Frame(fram2,width=174,height=600,borderwidth=3)

fram3 = ttk.Frame(mainfram, width=200, height=300, borderwidth=3)
# fram3_1=ttk.Frame(fram3,width=174,height=600,borderwidth=3)

fram4 = ttk.Frame(mainfram, width=200, height=300, borderwidth=3)
# fram4_1=ttk.Frame(fram4,width=174,height=600,borderwidth=3)
#
label1 = ttk.Label(fram1, text="InPutFile")
label2 = ttk.Label(fram1, text="OutPutDrictory")
label3 = ttk.Label(fram1, text="MaskFile")
label4 = ttk.Label(fram1, text="_Explain_\n\n\n")
label5 = ttk.Label(fram2, text="BackGroColor")
label6 = ttk.Label(fram2, background=choosecolorvar.get(), width=3)
label7 = ttk.Label(fram2, text="字体")
label8 = ttk.Label(fram2, text="Width")
label9 = ttk.Label(fram2, text="Height")
label10 = ttk.Label(fram2, text="100")
label11 = ttk.Label(fram2, text="100")
label16 = ttk.Label(fram2, text="MaxSize")
label12 = ttk.Label(fram2, text="Minsize")
label13 = ttk.Label(fram2, text="50")
label14 = ttk.Label(fram2, text="5")
label15 = ttk.Label(fram4, text="20")
#
entry1 = ttk.Entry(fram1, textvariable=evariable1, width=17)
entry2 = ttk.Entry(fram1, textvariable=evariable2, width=17)
entry3 = ttk.Entry(fram1, textvariable=evariable3, width=17)
#
btn1 = ttk.Button(fram1, text="choose...", command=getinputfile_btn1)
btn2 = ttk.Button(fram1, text="choose...", command=getsavefile_btn2)
btn3 = ttk.Button(fram1, text="choose...", command=getmaskfile_btn3)
btn4 = ttk.Button(fram3, text="choose...", command=getcolor_btn4)
btn5 = ttk.Button(fram4, text="Generate", command=generate)
btn6 = ttk.Button(fram4, text="Star Call", command=startcall)
btn7 = ttk.Button(fram3, text="choose", command=getfont_btn7)
#
text1 = tk.Text(mainfram, width=25, height=20)
text2 = tk.Text(mainfram, width=25, height=20)
text3 = tk.Text(mainfram, width=25, height=20)

text3.insert("1.0", "马保国\n混元功法")
#

#
scale1 = ttk.Scale(
    fram3,
    orient=tk.HORIZONTAL,
    from_=50,
    to=1920,
    variable=getwidthvar,
    command=getwidth_label10,
)

scale2 = ttk.Scale(
    fram3,
    orient=tk.HORIZONTAL,
    from_=20,
    to=1080,
    variable=getheightvar,
    command=getheight_label11,
)

scale3 = ttk.Scale(
    fram3,
    orient=tk.HORIZONTAL,
    from_=5,
    to=100,
    variable=getmaxsizevar,
    command=getmax_label13,
)

scale4 = ttk.Scale(
    fram3,
    orient=tk.HORIZONTAL,
    from_=1,
    to=50,
    variable=getminsizevar,
    command=getmin_label14,
)

scale5 = ttk.Scale(
    fram4,
    orient=tk.HORIZONTAL,
    from_=10,
    to=400,
    variable=getwordnumvar,
    command=getnum_label15,
)
#


# gridloc
#
mainfram.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
fram1.grid(row=0, column=0, columnspan=2)

fram2.grid(row=2, column=0)

fram3.grid(row=2, column=1)

fram4.grid(row=2, column=2)

fram3.rowconfigure(0, pad=10)
fram3.rowconfigure(1, pad=10)
fram3.rowconfigure(2, pad=10)
fram3.rowconfigure(3, pad=10)
fram3.rowconfigure(4, pad=10)
fram3.rowconfigure(5, pad=10)

fram2.rowconfigure(0, weight=1, pad=12)
fram2.rowconfigure(1, weight=1, pad=12)
fram2.rowconfigure(2, weight=1, pad=12)
fram2.rowconfigure(3, weight=1, pad=12)
fram2.rowconfigure(4, weight=1, pad=12)
fram2.rowconfigure(5, weight=1, pad=12)


#
text1.grid(row=1, column=0)
text2.grid(row=1, column=1)
text3.grid(row=1, column=2, sticky=(tk.W, tk.E, tk.S, tk.N))


#


#
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
#
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
#
label4.grid(row=3, column=0, columnspan=3)
#
btn1.grid(row=0, column=2)
btn2.grid(row=1, column=2)
btn3.grid(row=2, column=2)
btn4.grid(row=0)  # /////////////////////////
btn5.grid()  # /////////////////
btn6.grid()  # /////////////////////////
btn7.grid(row=1)
#
label5.grid(row=0, column=0)
label6.grid(row=0, column=1)
label7.grid(row=1, column=1)
label8.grid(row=2, column=0)
label10.grid(row=2, column=1)
label9.grid(row=3, column=0)
label11.grid(row=3, column=1)
label16.grid(row=4, column=0)
label13.grid(row=4, column=1)
label12.grid(row=5, column=0)
label14.grid(row=5, column=1)
label15.grid()
#
# combobox1.grid(row=1)
#
scale1.grid(row=2)
scale2.grid(row=3)
scale3.grid(row=4)
scale4.grid(row=5)
scale5.grid()
#
# funclinks


# 显示gif
canvas = tk.Canvas(mainfram, width=200, height=200, bg="white")
canvas.grid(row=0, column=2)
canvas.grid_propagate(0)
img = []


def display(event):
    global display
    while display:
        im = Image.open("C:/Users/QJL/Desktop/3891.gif")
        # GIF图片流的迭代器
        iter = ImageSequence.Iterator(im)

        # frame就是gif的每一帧，转换一下格式就能显示了
        for frame in iter:
            if display:
                pic = ImageTk.PhotoImage(frame)
                canvas.create_image((100, 100), image=pic)
                # sleep(0.1)
                root.after(100)
                # root.update_idletasks()  #刷新
                root.update()
    display = True


def stopdisplay(event):
    global display
    display = False
    print("1")


canvas.bind("<Enter>", display)  # 鼠标进入事件
canvas.bind("<Leave>", stopdisplay)  # 鼠标离开事件

root.mainloop()
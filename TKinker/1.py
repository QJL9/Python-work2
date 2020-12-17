from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
import fontchooser
from PIL import Image, ImageTk, ImageSequence
import time

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()

root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# mainframe.columnconfigure(weight=1)
# mainframe.rowconfigure(weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
a = ttk.Label(mainframe, text="meters")
a.grid(column=3, row=2, sticky=W)


canvas = Canvas(root,width=300, height=300,bg='white')
canvas.grid()
img=[]
#分解gif并逐帧显示
def display(event):
    global a,flag   
    while 1:
        im = Image.open(r'C:\Users\QJL\Desktop\3891.gif')
        # GIF图片流的迭代器
        iter = ImageSequence.Iterator(im)
        #frame就是gif的每一帧，转换一下格式就能显示了
        for frame in iter:
            pic=ImageTk.PhotoImage(frame)
            canvas.create_image((150,150), image=pic)
            time.sleep(0.1)
            root.update_idletasks()  #刷新
            root.update()

canvas.bind("<Enter>",display)  #这个事件是鼠标进入组件，用什么事件不重要，这里只是演示
root.mainloop()











for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)



b=fontchooser.askfont()
a['font'] = (b)



feet_entry.focus()
root.attributes("-alpha", 0.8)


root.bind("<Return>", calculate)

root.mainloop()
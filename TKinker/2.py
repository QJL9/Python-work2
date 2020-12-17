import tkinter as tk
#from tkinter.filedialog import askopenfilename

app = tk.Tk()
app.geometry('200x300')
app.title("window")

#stringvariable
strvar = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var3.set(0)
var2.set(['1','2','5','4','d','h','q','r'])
strvar.set('123')

#function
def abc():
    global strvar
    strvar.set(en.get())
    print(strvar)
    btn1.config(state='disabled')
def abc2():
    print(var3.get())



#widgets
lab1 = tk.Label(app,width='50',height=2,textvariable=strvar
,font=('Microsoft YaHei',20))

btn1=tk.Button(app,text="btn1",width=20,bg="gray",
command=abc)

tex = tk.Text(width=20,height=2)

en= tk.Entry(app)

lb = tk.Listbox(app,listvariable=var2)

rb1 = tk.Radiobutton(app,text='radiobutton1',
variable=var3,value='1',
command=abc2)
rb2 = tk.Radiobutton(app,text='radiobutton2',
variable=var3,value='2',
command=abc2)
rb3 = tk.Radiobutton(app,text='radiobutton3',state='normal',
variable=var3,value='3',
command=abc2)


#pack
tex.pack()
lab1.pack()
btn1.pack()
en.pack()
lb.pack()
rb1.pack()
rb2.pack()
rb3.pack()

app.mainloop()
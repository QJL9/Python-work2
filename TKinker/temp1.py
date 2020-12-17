import tkinter as tk
from tkinter import ttk
root = tk.Tk()

# s = ttk.Style()
# s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')

s = ttk.Style()
s.configure('asdfasf.TFrame',background='blue',borderwidth=2, relief='raised')
fram1= ttk.Frame(root,width=200,height=200,style='asdfasf.TFrame')
fram2= ttk.Frame(root,width=200,height=200,borderwidth=2,style='asdfasf.TFrame')
fram3= ttk.Frame(root,width=200,height=200,borderwidth=2,style='asdfasf.TFrame')
fram4= ttk.Frame(root,width=200,height=200,borderwidth=2,style='asdfasf.TFrame')
fram5= ttk.Frame(fram4,width=200,height=200,borderwidth=2)
fram1.grid(row=0,column=0)
fram2.grid(row=1,column=0)
fram3.grid(row=0,column=1)
fram4.grid(row=1,column=1)

fram5.grid()
label1=ttk.Label(fram5,text='label')
# btn1 = ttk.Button(fram1,text='button')
# #btn1.grid(row=0,column=0,sticky=(tk.N))
label1.grid(row=0,column=0,sticky=(tk.N),padx=5,pady=5)


# s = ttk.Style()
# s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
# fram1=ttk.Frame(root, width=200, height=200, style='Danger.TFrame')
# fram1.grid()
root.mainloop()
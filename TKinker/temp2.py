import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("Call_Master_Ma")
fram1=ttk.Frame(root,width=200,height=20,borderwidth=3)
fram1_1=ttk.Frame(fram1,width=200,height=20,borderwidth=3)

fram2=ttk.Frame(root,width=200,height=20,borderwidth=3)
#fram2_1=ttk.Frame(fram2,width=174,height=600,borderwidth=3)

fram3=ttk.Frame(root,width=200,height=20,borderwidth=3)
#fram3_1=ttk.Frame(fram3,width=174,height=600,borderwidth=3)

fram4=ttk.Frame(root,width=200,height=20,borderwidth=3)
#fram4_1=ttk.Frame(fram4,width=174,height=600,borderwidth=3)
btn1= ttk.Button(fram1_1,text='btn1')
btn2= ttk.Button(fram1_1,text='btn1')
btn3= ttk.Button(fram1_1,text='btn1')
btn4= ttk.Button(fram1_1,text='btn1')

fram1.grid(row=0,column=0)
fram1.grid_propagate(0)
fram1_1.grid(row=0,column=0)
fram1_1.grid_propagate(1)
fram2.grid(row=2,column=0)
fram2.grid_propagate(0)
fram3.grid(row=2,column=1)
fram3.grid_propagate(0)
fram4.grid(row=2,column=2)
fram4.grid_propagate(0)
btn1.grid()
btn2.grid()
btn3.grid()
btn4.grid()

root.mainloop()
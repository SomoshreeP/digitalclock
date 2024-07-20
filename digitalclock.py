from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p %a')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("times new roman", 50), background="green", foreground="pink")
label.pack(anchor='center')

time()
mainloop()
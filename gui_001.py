
from sqlite3 import Row
import tkinter as tk
from tkinter.tix import COLUMN
import turtle
window = tk.Tk()
window.title("my program")
window.geometry("500x200")

def Hello():
    pole = input1.get()
b_2 = tk.Button(window, text="button3", command=Hello )
b_2.grid(column=3, row=2)
input1 = tk.Entry(window, width='50')
input1.grid(column=2, row=0)
lbl_1 = tk.Label(window, text="Hello world!")
lbl_1.grid(column = 0, row  = 0)
lbl_2 = tk.Label(window, text="patnaka")
lbl_2.grid(column = 0, row  = 1)
lbl_3 = tk.Label(window, text="Gui top!")
lbl_3.grid(column = 0, row  = 2)
b = tk.Button(window, text="button1")
b.grid(column=1, row=0)

b_1 = tk.Button(window, text="button2")
b_1.grid(column=2, row=1)



window.mainloop()
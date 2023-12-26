
import tkinter as tk
window = tk.Tk()

def s():
    p = input_1.get()
    p2 = input_2.get()
    File = open("s.txt", 'a')
    File.write(p)
    File.write(p2)
label_1 = tk.Label(window, text="festname")
label_1.grid(column=0, row=0)
input_1 = tk.Entry(window, width=50)
input_1.grid(column=1, row=1)
label_2 = tk.Label(window, text="lastname")
label_2.grid(column=3, row=3)
input_2 = tk.Entry(window, width=50)
input_2.grid(column=4, row=4)
butt = tk.Button(window, text="s", command=s)
butt.grid(column=5, row=5)
window.mainloop()

import tkinter as tk
import turtle
t = turtle.Turtle()
def up():
    t.forward(30)  
def lt():
    t.left(90)  
def rt():
    t.right(90)  
def dn():
    t.backward(30)  
def pn():
    t.penup()
def pd():
    t.pendown()                 
w = tk.Tk()
w.title("GAME")
w.geometry("250x100")
btn_up = tk.Button(w, text="UP", command = up)
btn_up.grid(column = 3, row = 0)
btn_left = tk.Button(w, text="LEFT", command = lt)
btn_left.grid(column = 1, row = 1)
btn_right = tk.Button(w, text="RIGHT", command = rt)
btn_right.grid(column = 6, row = 1)
btn_down = tk.Button(w, text="DOWN", command = dn)
btn_down.grid(column = 3, row = 2)
btn_pnup = tk.Button(w, text = "PEN UP", command = pn)
btn_pnup.grid(column = 10, row = 0)
btn_pndn = tk.Button(w, text = "PEN DOWN", command = pd)
btn_pndn.grid(column = 10, row = 2)
w.mainloop()
import tkinter
from tkinter import *
import 

global width,height

def center(win):
    global width,height
    a=150
    b=300
    win.update_idletasks()
    width = win.winfo_width()+a
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()+b
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width+20
    x = win.winfo_screenwidth() // 2 - win_width//2  
    y = win.winfo_screenheight() // 2 - win_height//2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


root = tkinter.Tk()
center(root)
root.title(" "*(width//8-3)+"JARVIS")
root.resizable(0,0)

bg = PhotoImage(file = "AI BG.png")
bg_lb = Label( root, image = bg)
bg_lb.place(x = -2, y = -2)

#=================================Listen-Speak Button================================
global mk_on,mk_off,sun_lb

def Silent():
    global mk_off,sun_lb
    mk_b1.configure(image=mk_off, command=lambda : Listen())
    sun_lb.destroy()
    

def Listen():
    global mk_on,sun_lb
    sun_lb=Label(root, text="Listening...")
    sun_lb.pack()
    mk_b1.configure(image=mk_on, command=lambda : Silent())

mk_off = PhotoImage(file = "mike-off.png")
mk_on = PhotoImage(file = "mike-on.png")

mk_b1 = Button( root, image = mk_off, bg="Black", command=lambda : Listen())
mk_b1.place(x = width-40, y = height-40)

    


root.mainloop()

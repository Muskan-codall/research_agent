from tkinter import *

root =Tk()

l1 =Label(text="you")
l1.pack()
t1 =Entry()
t1.pack()
l3 =Text()
l3.pack()

def show():
    root.destroy()
    import main  

Button(text="enter",command=show).pack()
Button(text="submit",command=work)
mainloop()
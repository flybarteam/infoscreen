from tkinter import *

def Bergen():
    master = Tk()
    master.title("Bergen")
    w = Label(master, text="Velkommen til Bergen",
    width=100, height=2, bg="light slate blue")
    w.config(font=("Courier", 44))
    w.pack()
    master.after(10000, master.destroy)              #The time, the label stands, before it is destroyed.
    master.mainloop()

Bergen()
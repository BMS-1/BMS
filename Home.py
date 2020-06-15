from tkinter import *


def gotomehsana(self):
    print("kashyap")
class home:
    def __init__(self):
        root.geometry ( "700x500" )
        menu=Menu(root)
        root.config(menu=menu)

        subMenu=Menu(menu)
        menu.add_cascade(label="location", menu=subMenu)
        subMenu.add_command(label="mehsana",command=gotomehsana(self))








root=Tk ()
start=home()
root.mainloop()



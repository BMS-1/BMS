from tkinter import *


def gotobollywood(self):
    print("kashyap")


def gotohollywood(self):
    print("urmil")


def gotoahmedabad(self):
    print("")


def gotomeshana(self):
    print("kashyap")


def gotoenglish(self):
    print("urmil")


def gotohindi(self):
    print("urmil")


def gotogujarati(self):
    print("urmil")


def gotooff1(self):
    print("urmil")


def gotooff2(self):
    print("urmil")


def gotooff3(self):
    print("urmil")


class home:

    def __init__(self):
        root.geometry("900x600")

        root.title("BOOK MY SHOW")
        mylabel = Label(root, text="BOOK MY SHOW", font=184)
        mylabel.grid(row=0, column=3, columnspan=2)
        menu = Menu(root)
        root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Movies", menu=subMenu)
        subMenu.add_command(label="bollywood", command=gotobollywood(self))
        subMenu.add_command(label="hollywood", command=gotohollywood(self))

        subMen = Menu(menu)
        menu.add_cascade(label="location", menu=subMen)
        subMen.add_command(label="ahmedabad", command=gotoahmedabad(self))
        subMen.add_command(label="meshana", command=gotomeshana(self))

        subMen1 = Menu(menu)
        menu.add_cascade(label="language", menu=subMen1)
        subMen1.add_command(label="english", command=gotoenglish(self))
        subMen1.add_command(label="hindi", command=gotohindi(self))
        subMen1.add_command(label="gujarati", command=gotogujarati(self))

        subMen2 = Menu(menu)
        menu.add_cascade(label="offers", menu=subMen2)
        subMen2.add_command(label="10% off with creditcard", command=gotooff1(self))
        subMen2.add_command(label="30% off on every friday  ", command=gotooff2(self))
        subMen2.add_command(label="15% off with bms wallet", command=gotooff3(self))


root = Tk()

start = home()

root.geometry("810x450")

photo1 = PhotoImage(file="1.png")
lab1 = Label(root, image=photo1)
lab1.grid(row=1, column=0)

b1 = Button(root, text="booking").grid(row=0, column=0)

photo2 = PhotoImage(file="1.png")
lab2 = Label(root, image=photo2)
lab2.grid(row=1, column=7)

b2 = Button(root, text="offer").grid(row=0, column=7)

photo3 = PhotoImage(file="1.png")
lab3 = Label(root, image=photo3)
lab3.grid(row=8, column=3, columnspan=2)

b3 = Button(root, text="trending").grid(row=7, column=3, columnspan=2)

root.mainloop()




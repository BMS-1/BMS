from tkinter import *
global frame


def gotobollywood(self):
    pass

def gotobookingform():
    root = Tk()
    root.geometry("600x700")
    root.title("BOOK MY SHOW")

    label = Label(root, text="BOOKING FORM", relief="solid", width="122", font="88")
    label.pack()

    t0_text = Label(root,text="CUSTOMER NAME *", relief="solid")
    t1_text = Label(root,text="MOVIE NAME *", relief="solid")
    t2_text = Label(root,text="SEAT TIER *", relief="solid")
    t3_text = Label(root,text="PAYMENT METHOD *", relief="solid")
    t4_text = Label(root,text="LOCATION *", relief="solid")
    t5_text = Label(root,text="AVAIL OFFERS ", relief="solid")

    t0_text.place(x=240, y=70)
    t1_text.place(x=250, y=140)
    t2_text.place(x=260, y=210)
    t3_text.place(x=240, y=280)
    t4_text.place(x=259, y=350)
    t5_text.place(x=250, y=420)

    t0 = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t5 = StringVar()

    def printt():
        C = t0.get()
        M = t1.get()
        var4 = var3.get()
        P = t3.get()
        var1 = var.get()
        A = t5.get()

        print(C)
        print(M)
        print(var4)
        print(P)
        print(var1)
        print(A)

    def exitt():
        exit()

    t0_entry = Entry(root,textvariable=t0, width="30")
    t1_entry = Entry(root,textvariable=t1, width="30")

    t3_entry = Entry(root,textvariable=t3, width="30")

    t5_entry = Entry(root,textvariable=t5, width="30")

    t0_entry.place(x=205, y=100)
    t1_entry.place(x=205, y=170)

    t3_entry.place(x=205, y=310)

    t5_entry.place(x=205, y=450)

    b1 = Button(root, text="CONFIRM", bg="green", command=printt).place(x=205, y=505)
    b2 = Button(root, text="BACK", bg="red", command=exit).place(x=325, y=505)

    t4 = Label(root)
    t4.place(x=205, y=388)

    var = StringVar()

    list1 = ['ahmedabad', 'meshana', 'banglore']
    droplist = OptionMenu(root, var, *list1)
    var.set("SELECT")
    droplist.place(x=250, y=375)

    t2 = Label(root)
    t2.place(x=205, y=388)

    var3 = StringVar()

    list2 = ['Gold', 'Silver', 'Platinum']
    droplist1 = OptionMenu(root, var3, *list2)
    var3.set("SELECT")
    droplist1.place(x=250, y=236)

    root.mainloop()


def gotohollywood(self):
    pass


def gotoahmedabad(self):
    pass

def gotomehsana():
    root1=Toplevel(root)

    root1.geometry("1000x700")
    root1.title("mehsana")
    l1 = LabelFrame(root1, text="", padx=50, pady=10, bg="black")
    l1.grid(row=0, column=1)
    l2 = Label(root1, text="mehsana", fg="black", bg="gold", padx=30)
    l2.grid(row=0, column=2)
    l3 = Label(root1, text="             ", bg="royal blue", padx=30, )
    l3.grid(row=0, column=0)
    l4 = Label(root1, text="             ", bg="royal blue", padx=20, pady=15)
    l4.grid(row=1, column=2)
    l6 = LabelFrame(root1, text="", padx=40, pady=10, bg="black")
    l6.grid(row=2, column=0)
    l20 = LabelFrame(root1, text="", padx=170, pady=10, bg="black")
    l20.grid(row=2, column=1, columnspan=16)
    l21 = Label(l20, text="book my show", bg="gold", padx=40, pady=6)
    l21.grid(row=2, column=0)

    l5 = Label(l6, text=" wide angle", bg="gold", padx=30, pady=6)
    l5.grid(row=2, column=0)
    #  l7 = LabelFrame(root, text="", padx=155, pady=50, bg="grey")
    # l7.grid(row=4, column=1)
    l8 = Label(root1, text="wide angle ,mehsana" + "\n" + "rating=4/5", fg="black", bg="plum2", padx=30)
    l8.grid(row=4, column=1)
    l9 = Label(root1, text="             ", bg="royal blue", padx=20, pady=5)
    l9.grid(row=5, column=0)
    b1 = Button(root1, text="Book your ticket", bg="black", fg="white", command=gotobookingform)
    b1.grid(row=4, column=2)
    l12 = LabelFrame(root1, text="", padx=40, pady=10, bg="black")
    l12.grid(row=9, column=0)
    l18 = LabelFrame(root1, text="", padx=170, pady=10, bg="black")
    l18.grid(row=9, column=1, columnspan=16)
    l19 = Label(root1,text="book my show", bg="gold", padx=40, pady=6)
    l19.grid(row=2, column=0)
    l13 = Label(l12, text=" yoro club", bg="gold", padx=30, pady=6)
    l13.grid(row=9, column=0)
    l16 = Label(root1, text="             ", bg="royal blue", padx=30, )
    l16.grid(row=8, column=0)

    l14 = Label(root1, text="yoro club,mehsana" + "\n" + "rating=4/5", fg="black", bg="plum2", padx=30)
    l14.grid(row=10, column=1)

    b2 = Button(root1, text="Book your ticket", bg="black", fg="white", command=gotobookingform)
    b2.grid(row=10, column=2)

    l17 = Label(root1, text="", bg="royal blue")
    l17.grid(row=10, column=3)

    root1.config(bg="royal blue")

    photo = PhotoImage(file="1.png")
    label = Label(root1,image=photo, bg="black")
    label.grid(row=4, column=0, rowspan=3)
    photo3 = PhotoImage(file="4.png")
    label4 = Label(root1,image=photo3, bg="black")
    label4.grid(row=4, column=4, rowspan=3)

    photo1 = PhotoImage(file="2.png")
    label1 = Label(root1,image=photo1, bg="black")
    label1.grid(row=10, column=0, rowspan=3)
    photo2 = PhotoImage(file="3.png")
    label1 = Label(root1,image=photo2, bg="black")
    label1.grid(row=10, column=4, rowspan=3)

    root.mainloop()

def gotoenglish(self):
    pass


def gotohindi(self):
    pass


def gotogujarati(self):
    pass


def gotooff1(self):
    pass


def gotooff2(self):
    pass


def gotooff3(self):
    pass

def main_home():
    global root
    root = Tk()

    root.geometry("900x600")

    root.title("BOOK MY SHOW")
    mylabel = Label(root, text="BOOK MY SHOW", font=184)
    mylabel.grid(row=0, column=3, columnspan=2)
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Movies", menu=subMenu)
    subMenu.add_command(label="bollywood", command=gotobollywood)
    subMenu.add_command(label="hollywood", command=gotohollywood)

    subMen = Menu(menu)
    menu.add_cascade(label="location", menu=subMen)
    subMen.add_command(label="ahmedabad", command=gotoahmedabad)
    subMen.add_command(label="mehsana", command=gotomehsana)

    subMen1 = Menu(menu)
    menu.add_cascade(label="language", menu=subMen1)
    subMen1.add_command(label="english", command=gotoenglish)
    subMen1.add_command(label="hindi", command=gotohindi)
    subMen1.add_command(label="gujarati", command=gotogujarati)

    subMen2 = Menu(menu)
    menu.add_cascade(label="offers", menu=subMen2)
    subMen2.add_command(label="10% off with creditcard", command=gotooff1)
    subMen2.add_command(label="30% off on every friday  ", command=gotooff2)
    subMen2.add_command(label="15% off with bms wallet", command=gotooff3)



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

main_home()


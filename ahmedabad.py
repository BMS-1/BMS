from tkinter import *
global frame

def gotobookingform():
    print("kashyap")


class mehsana:
    def __init__(self):
        root.geometry("715x500")
        root.title("Ahmedabad")
        l1=LabelFrame(root,text="",padx=50,pady=10,bg="black")
        l1.grid(row=0,column=1)
        l2=Label(l1,text="Ahmedabad",fg="black",bg="gold",padx=30)
        l2.grid(row=0,column=2)
        l3 = Label(root, text="             ",bg="royal blue", padx=30,)
        l3.grid(row=0, column=0)
        l4 = Label(root, text="             ", bg="royal blue", padx=20, pady=15)
        l4.grid(row=1, column=2)
        l6 = LabelFrame(root, text="", padx=40, pady=10, bg="black")
        l6.grid(row=2, column=0)
        l20 = LabelFrame(root, text="", padx=170, pady=10, bg="black")
        l20.grid(row=2, column=1, columnspan=16)
        l21 = Label(l20, text="book my show", bg="gold", padx=40, pady=6)
        l21.grid(row=2, column=0)

        l5 = Label(l6, text="City gold", bg="gold", padx=30, pady=6)
        l5.grid(row=2, column=0)
      #  l7 = LabelFrame(root, text="", padx=155, pady=50, bg="grey")
       # l7.grid(row=4, column=1)
        l8= Label(root, text="City gold ,driving road"+"\n"+"rating=4/5", fg="black", bg="plum2",padx=30)
        l8.grid(row=4,column=1)
        l9 = Label(root, text="             ", bg="royal blue", padx=20, pady=5)
        l9.grid(row=5, column=0)
        b1=Button(root,text="Book your ticket",bg="black",fg="white",command=gotobookingform)
        b1.grid(row=4,column=2)
        l12 = LabelFrame(root, text="", padx=40, pady=10, bg="black")
        l12.grid(row=9, column=0)
        l18 = LabelFrame(root,  text="", padx=170, pady=10, bg="black")
        l18.grid(row=9, column=1,columnspan=16)
        l19 = Label(l18, text="book my show", bg="gold", padx=40, pady=6)
        l19.grid(row=2, column=0)
        l13 = Label(l12, text=" PVR",bg="gold", padx=55, pady=6)
        l13.grid(row=9, column=0)
        l16 = Label(root, text="             ", bg="royal blue", padx=30, )
        l16.grid(row=8, column=0)

        l14 = Label(root, text="PVR,vastrapur" + "\n" + "rating=4/5", fg="black", bg="plum2", padx=30)
        l14.grid(row=10, column=1)

        b2 = Button(root, text="Book your ticket", bg="black", fg="white", command=gotobookingform)
        b2.grid(row=10, column=2)

        l17 = Label(root, text="", bg="royal blue")
        l17.grid(row=10, column=3)

        root.config(bg="royal blue")








root=Tk()
meh=mehsana()
photo = PhotoImage(file="1.png")
label = Label(image=photo,bg="black",width=200,height=130)
label.grid(row=4,column=0,rowspan=3)
photo3 = PhotoImage(file="4.png")
label4 = Label(image=photo3,bg="black",width=180,height=130)
label4.grid(row=4,column=4,rowspan=3)

photo1 = PhotoImage(file="2.png")
label1 = Label(image=photo1,bg="black",width=190,height=130)
label1.grid(row=10,column=0,rowspan=3)
photo2 = PhotoImage(file="3.png")
label1 = Label(image=photo2,bg="black",width=180,height=130)
label1.grid(row=10,column=4,rowspan=3)




root.mainloop()
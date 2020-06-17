from tkinter import *

root = Tk()
root.geometry("600x700")
root.title("BOOK MY SHOW")



label=Label(root,text="BOOKING FORM",relief="solid",width="122",font="88")
label.pack()

t0_text=Label(text="CUSTOMER NAME *",relief="solid")
t1_text=Label(text="MOVIE NAME *",relief="solid")
t2_text=Label(text="SEAT TIER *",relief="solid")
t3_text=Label(text="PAYMENT METHOD *",relief="solid")
t4_text=Label(text="LOCATION *",relief="solid")
t5_text=Label(text="AVAIL OFFERS ",relief="solid")

t0_text.place(x=240,y=70)
t1_text.place(x=250,y=140)
t2_text.place(x=260,y=210)
t3_text.place(x=240,y=280)
t4_text.place(x=259,y=350)
t5_text.place(x=250,y=420)


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
    print(var1 )
    print( A )

def exitt():
    exit()


t0_entry= Entry(textvariable=t0,width="30")
t1_entry=Entry(textvariable=t1,width="30")

t3_entry=Entry(textvariable=t3,width="30")

t5_entry=Entry(textvariable=t5,width="30")



t0_entry.place(x=205,y=100)
t1_entry.place(x=205,y=170)

t3_entry.place(x=205,y=310)

t5_entry.place(x=205,y=450)

b1=Button(root,text="CONFIRM",bg="green",command=printt).place(x=205,y=505)
b2=Button(root,text="BACK",bg="red",command=exit).place(x=325,y=505)


t4=Label(root)
t4.place(x=205,y=388)


var=StringVar()

list1=['ahmedabad','meshana','banglore']
droplist=OptionMenu(root,var,*list1)
var.set("SELECT" )
droplist.place(x=250,y=375)

t2=Label(root)
t2.place(x=205,y=388)


var3=StringVar()

list2=['Gold','Silver','Platinum']
droplist1=OptionMenu(root,var3,*list2)
var3.set("SELECT" )
droplist1.place(x=250,y=236)



root.mainloop()
from tkinter import *
import os


def login_verify():


    u1=username_verify.get()
    p1=password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files=os.listdir()
    if u1 in list_of_files:
        file1=open(u1,"r")
        verify=file1.read().splitlines()

        if p1 in verify:
            login_success()
        else:
            password_not_recognised()

    else:
        user_not_found()

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def login_success():

    global screen3
    screen3=Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("250x80")

    Label(screen3,text="Login Success",fg="green",padx=80).grid(row=0,column=28,columnspan=10)
    Button(screen3,text="OK",command=delete2).grid(row=1,column=28,columnspan=10)

def password_not_recognised():

    global screen4
    screen4=Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("250x80")
    Label(screen4, text="Password error",fg="red",padx=80).grid(row=0,column=28,columnspan=10)
    Button(screen4, text="OK", command=delete3).grid(row=1,column=28,columnspan=10)


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("250x80")
    Label(screen5, text="User not found",fg="red",padx=80).grid(row=0, column=10, columnspan=5)
    Button(screen5, text="OK", command=delete4).grid(row=1, column=10, columnspan=5)

def delete4():
    screen5.destroy()

def register_user():

    username_info=username.get()
    password_info=password.get()

    file=open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    u1.delete(0, END)
    p1.delete(0, END)

    Label(screen1,text="Register Success", fg="green").grid(row=0,column=28,columnspan=10)

def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global u1
    global p1

    username= StringVar()
    password= StringVar()

    Label(screen1, text="Please enter detail",padx=80).grid(row=0,column=28,columnspan=10)
    Label(screen1,text="").grid(row=1,column=28,columnspan=2)
    Label(screen1,text="Username *",padx=80).grid(row=2,column=28,columnspan=10)
    u1=Entry(screen1,textvariable=username)
    u1.grid(row=3,column=28,columnspan=10)

    Label(screen1,text="Password *",padx=80).grid(row=5,column=28,columnspan=10)
    p1=Entry(screen1, textvariable=password)
    p1.grid(row=6,column=28,columnspan=10)

    Label(screen1, text="").grid(row=7,column=28,columnspan=10)

    Button(screen1,text="Register",padx=80,command=register_user).grid(row=9,column=28,columnspan=10)

def login():

    global screen2
    global password_entry1
    global username_entry1
    global username_verify
    global password_verify


    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")


    Label(screen2,text="Pls enter login details",padx=80).grid(row=0,column=28,columnspan=10)
    Label(screen2,text="").grid(row=1,column=28,columnspan=10)
    username_verify=StringVar()
    password_verify=StringVar()

    Label(screen2, text="Username",padx=80).grid(row=2, column=28, columnspan=10)
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.grid(row=3,column=28,columnspan=10)
    Label(screen2, text="").grid(row=4, column=28, columnspan=10)
    Label(screen2,text="Password",padx=80).grid(row=5, column=28, columnspan=10)
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.grid(row=6,column=28,columnspan=10)
    Button(screen2,text="Login",width=5,height=2,command=login_verify).grid(row=7,  column=28, columnspan=10)

def main_screen():
    global screen
    screen = Tk()

    screen.geometry("300x200")
    screen.title("Sign Up Page")

    l1 = Label(screen, text="Sign Up Page", bg="grey",width=40,height=2).grid(row=0,column=40,columnspan=3)
    l2 = Label(screen, text="").grid(row=1,column=1)
    b1 = Button(screen, text="Login", height=2, width=5,padx=10,command=login).grid(row=2,column=40,columnspan=3)
    l3 = Label(screen, text="").grid(row=3,column=1)
    b2 = Button(screen, text="Register", height=2 , width=5,padx=10,command=register).grid(row=4,column=40,columnspan=3)
    screen.mainloop()



main_screen()
from tkinter import  *

class mehsana:
    def __init__(self):
        root.geometry("700x500")
        root.title("mehsana")







root=Tk()
meh=mehsana()
photo = PhotoImage(file="1.png")
label = Label(image=photo,bg="black")
label.pack(side=TOP)

root.mainloop()
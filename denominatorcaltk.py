from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denominator Counter')
root.configure(bg='lightblue')
root.geometry('800x600')

upload = Image.open("")

upload = upload.resize((800, 600))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='lightblue')
label.place(x=0, y=0)

label2 = Label(root, 
               text="This is a denominator counter window", bg='lightblue', font=('Arial', 16))
label2.place(relx=0.5, rely=0.1, anchor='n')

def show_message():
    messagebox.showinfo("Info", "This is a denominator counter application.")
    if MsgBox == 'yes':
        topwin()
def topwin():

 button1 = Button(root, text="Show Info", command=show_message, bg='lightgreen', font=('Arial', 14))

 button1.place(relx=0.5, rely=0.2, anchor='n')

def topwin():
    top = Toplevel()
    top.title("Top Window")
    top.configure(bg='lightblue')
    top.geometry('400x300+50+50')

    label = Label(top, text="enter your denominator", bg='lightblue', font=('Arial', 14))
    entry = Entry(top)
    lbl = Label(top, text="Denominator:", bg='lightblue')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amout
            amout = int(entry.get())
            note2000 = amout // 2000
            amout = amout % 2000
            note500 = amout // 500
            amout = amout % 500
            note100 = amout // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, note2000)
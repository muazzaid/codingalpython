from tkinter import *

window = Tk()
window.title('tkinter sample window')
window.geometry('400x400')

greenting = Label(window, text='Hello, Tkinter!')
button = Button(window, text='Click Me', bg='blue', fg='white')
entry = Entry(window, width=20)
greenting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=2)
frame.pack()
label = Label(master=frame, text='sample Frame')
label.pack()

textbox = Text(fg='black', bg='lightgrey', width=30, height=10)
textbox.pack()
window.mainloop()
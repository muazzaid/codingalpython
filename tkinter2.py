import tkinter as tk

window = tk.Tk()

for i in range(5):
    for j in range(5):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Frame {i},{j}')
        label.pack()

window.mainloop()
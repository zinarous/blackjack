from tkinter import *

root = Tk()
root.title("BlackJack")
root.geometry("1920x1080")
root.config(bg='green')
root.columnconfigure(0, minsize=650)
root.rowconfigure([0, 1], minsize=100)
btn = Button(text="Начать игру!", height = 4, width = 20, font = '16')
btn.grid(row = 2, column = 1, padx = 5, pady = 5)
photo = PhotoImage(file = "project/title.gif")
label = Label(image = photo)
label.grid(row = 1, column = 1, padx = 5, pady = 5)
root.mainloop()
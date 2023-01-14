import tkinter
from random import randint
from tkinter import messagebox
from tkinter import END
from book import Book
import booksSDK


"""
    low = 0
    high = 20
    rand = randint(low, high)

    def check(guess):
        if guess < rand:
            tkinter.messagebox.showinfo("Alert",f"{guess} was too low!")
        elif guess > rand:
            tkinter.messagebox.showinfo("Alert",f"{guess} was too high!")
        else:
            tkinter.messagebox.showinfo("Alert",f"Poggers! You won, {guess} was correct!")

    tk = tkinter.Tk()
    tk.title("Application Title")

    label = tkinter.Label(tk, text=f"Guess a number {low} to {high}")
    label.pack()

    entry = tkinter.Entry(tk)
    entry.pack()

    button = tkinter.Button(tk,text="Guess",command=lambda: check(int(entry.get())))
    button.pack()
"""

booksLocal = []

def add_to_list():
    if not titleEntry.get() == "" and not pageEntry.get() == "":
        book = Book(titleEntry.get(),pageEntry.get())

        if(booksSDK.add_book(book)):
            booksLocal.append(book)
            listbox.insert(END, book)
            titleEntry.delete(0,END)
            pageEntry.delete(0,END)

def remove_from_list():
    indexBook = listbox.curselection()
    book = booksLocal.pop(indexBook[0])
    if(booksSDK.delete_book(book)):
        listbox.delete(indexBook)


tk = tkinter.Tk()
tk.title("Add and Remove List")

listbox = tkinter.Listbox(tk)
listbox.pack()

for book in booksSDK.get_books():
    booksLocal.append(book)
    listbox.insert(END,book)

title = tkinter.Label(tk, text="Book Title:")
title.pack()

titleEntry = tkinter.Entry(tk)
titleEntry.pack()

pages = tkinter.Label(tk, text="Book Pages:")
pages.pack()

pageEntry = tkinter.Entry(tk)
pageEntry.pack()

button = tkinter.Button(tk, text="Add Book", command=add_to_list)
button.pack()

button = tkinter.Button(tk, text="Remove Selected Book", command=remove_from_list)
button.pack()

tk.mainloop()

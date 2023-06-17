import wikipedia as wk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Wikipedia parser")
root.geometry("200x100+750+200")
root.resizable(False, False)
text = ""


def get_value():
    global text
    text = entry.get()
    search()


def search():
    wk.set_lang('en')
    try:
        page = wk.page(text)
        with open('file.txt', 'w', encoding='utf-8') as file:
            file.write(f"{page.original_title}")
            file.write(f"\n{page.summary}")
            file.write(f"\nFrom: {page.url}")
    except wk.exceptions.DisambiguationError as e:
        messagebox.showerror("Error", "Please input konkretnoe znacenie")

label = Label(text="Enter your request:")
entry = Entry()
button = Button(text="Search", command=get_value)


label.pack()
entry.pack()
button.pack()


root.mainloop()

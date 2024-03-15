import random
import string
from tkinter import *

def generate_password():
    password_length = int(entry_length.get())
    include_lowercase = var_lowercase.get()
    include_uppercase = var_uppercase.get()
    include_digits = var_digits.get()
    include_symbols = var_symbols.get()

    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Please select at least one type of characters.")
        return

    password = ''.join(random.choice(characters) for i in range(password_length))
    result_label.config(text=password)

# GUI setup
root = Tk()
root.title("Password Generator")

frame = Frame(root)
frame.pack(pady=10)

label_length = Label(frame, text="Password Length:")
label_length.grid(row=0, column=0)

entry_length = Entry(frame)
entry_length.grid(row=0, column=1)
entry_length.insert(0, " ") 

var_lowercase = BooleanVar()
var_uppercase = BooleanVar()
var_digits = BooleanVar()
var_symbols = BooleanVar()

check_lowercase = Checkbutton(frame, text="Lowercase", variable=var_lowercase)
check_lowercase.grid(row=1, column=0, sticky=W)
check_lowercase.select()

check_uppercase = Checkbutton(frame, text="Uppercase", variable=var_uppercase)
check_uppercase.grid(row=1, column=1, sticky=W)
check_uppercase.select()

check_digits = Checkbutton(frame, text="Digits", variable=var_digits)
check_digits.grid(row=2, column=0, sticky=W)
check_digits.select()

check_symbols = Checkbutton(frame, text="Symbols", variable=var_symbols)
check_symbols.grid(row=2, column=1, sticky=W)

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 12), wraplength=300)
result_label.pack()

root.mainloop()
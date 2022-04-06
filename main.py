from tkinter import *
import random
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


def password_gen():
    global DIGITS
    global LOCASE_CHARACTERS
    global UPCASE_CHARACTERS
    global SYMBOLS
    password = []
    for i in range(0, 3):
        number = random.choice(DIGITS)
        password.append(number)
        upcase = random.choice(UPCASE_CHARACTERS)
        password.append(upcase)
        locase = random.choice(LOCASE_CHARACTERS)
        password.append(locase)
        symb = random.choice(SYMBOLS)
        password.append(symb)
    secret = ''.join(password)
    pass_input.delete(0, END)
    pass_input.insert(0, secret)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    website = website_input.get()
    username = username_input.get()
    password = pass_input.get()

    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Error",message="Enter all the Values")

    else:
        is_ok = messagebox.askokcancel(title="Password Save?", message="Save login details?")
        if is_ok:
            with open('Passwords.txt', 'a') as file:
                file.write(f"Website: {website}|Username: {username}|Password: {password}\n")
                website_input.delete(0, END)
                username_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()

website_input.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Website/Email :")

username_label.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.insert(0, string="promit.xi@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky='EW')

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3, sticky='EW')

pass_gen = Button(text="Generate", command=password_gen)
pass_gen.grid(column=2, row=3)

add_pass = Button(text="Store", width=36, command=write_to_file)
add_pass.grid(column=1, row=4, columnspan=2)

label_palavan = Label(text="PalaVan Widgets", fg="#4D96FF", font=("Gabriola", 12, 'bold'), highlightthickness=0)
label_palavan.grid(column=1, row=5)

window.mainloop()

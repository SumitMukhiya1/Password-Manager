from tkinter import *
from tkinter import messagebox
import random
from random import randint, choice
import json


#________________________________________________________________Generate Password_______________________________________________________________

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)
  password = "".join(password_list)
  password_entry.delete(0, END)
  password_entry.insert(0, password)





# ________________________________________________________________Save Password_______________________________________________________________
def save():
  website = website_entry.get()
  email = email_entry.get()
  user_password = password_entry.get()
  new_data = {
    website:{
      "email": email,
      "password": user_password,

  }}

  # Check if any field is empty
  if len(website) == 0 or len(user_password) == 0:
    messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
  else:
    try:
      with open("data.json", "r") as data_file:
        data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # If file doesn't exist or is invalid

    # Update data
    data.update(new_data)

    # Write back to file
    with open("data.json", "w") as data_file:
      json.dump(data, data_file, indent=4)
      # Clear entries
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No DataFile Found.")
    else:
        if website in data:
           email = data[website]["email"]
           password = data[website]["password"]
           messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Data Not Found", message=f"Please Create A website password")





#_________________________________________________________________UI SETUP___________________________________________________________________
# window = Tk()
# window.title("Password Manager")
# window.config(padx=50,pady=50, bg="white")
#
# canvas = Canvas(width=260, height=260, bg="white",highlightthickness=0)
# logo = PhotoImage(file="logo.png")
# canvas.create_image(130, 130, image=logo)
# canvas.grid(row=0, column=1)
#
# #Labels
# website_label = Label(text="Website:", bg="white", fg="black")
# email_label = Label(text="Email/UserName:", bg="white", fg="black")
# password_label = Label(text="Password:", bg="white", fg="black")
# website_label.grid(column=0, row=1)
# email_label.grid(column=0, row=2)
# password_label.grid(column=0, row=3)
#
# #Entries
# website_entry = Entry(width=53, bg="white", fg="black")
# website_entry.focus()
# email_entry = Entry(width=53, bg="white", fg="black")
# email_entry.insert(0, "sumitmukhiya@gmail.com")
# password_entry = Entry(width=43, bg="white", fg="black")
# website_entry.grid(column=1, row=1, columnspan=2)
# email_entry.grid(column=1, row=2, columnspan=2)
# password_entry.grid(column=1, row=3)
#
# #Buttons
# generate_password_button = Button(text="Generate", bg="white", fg="black", command=generate_password)
# add_button = Radiobutton(text="Add", bg="#470000",fg="white", width=42, command=save)
# search_button = Button(text="Search", bg="white", fg="black")
# generate_password_button.grid(column=2, row=3)
# add_button.grid(column=1, row=4, columnspan=2)
# search_button.grid()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Canvas with logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", fg="black", font=("Arial", 10))
email_label = Label(text="Email/Username:", bg="white", fg="black", font=("Arial", 10))
password_label = Label(text="Password:", bg="white", fg="black", font=("Arial", 10))

website_label.grid(column=0, row=1, sticky="e", padx=(0, 10), pady=5)
email_label.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=5)
password_label.grid(column=0, row=3, sticky="e", padx=(0, 10), pady=5)

# Entries
website_entry = Entry(width=32, bg="white", fg="black", font=("Arial", 10))
website_entry.focus()
email_entry = Entry(width=32, bg="white", fg="black", font=("Arial", 10))
email_entry.insert(0, "sumitmukhiya@gmail.com")
password_entry = Entry(width=21, bg="white", fg="black", font=("Arial", 10))

website_entry.grid(column=1, row=1, sticky="ew", pady=5)
email_entry.grid(column=1, row=2, sticky="ew", pady=5, columnspan=2)
password_entry.grid(column=1, row=3, sticky="w", pady=5)

# Buttons (Fixed: Using Button instead of Radiobutton)
search_button = Button(text="Search", bg="white", fg="black", width=14, font=("Arial", 10), command=find_password)
generate_password_button = Button(text="Generate Password", bg="white", fg="black", width=14, font=("Arial", 10), command=generate_password)
add_button = Button(text="Add", bg="#470000", fg="white", width=44, font=("Arial", 10, "bold"), command=save)

search_button.grid(column=2, row=1, padx=(10, 0), pady=5)
generate_password_button.grid(column=2, row=3, padx=(10, 0), pady=5)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

# Make the grid responsive
window.columnconfigure(1, weight=1)

window.mainloop()






window.mainloop()
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_user_info():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Warning: Empty Field(s)",message="Please fill in all the fields!")
    else:
        is_okay = messagebox.askokcancel(title="Please Confirm",message=f"website: {website},\nemail: {email},\npassword: {password}")

        if is_okay:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    data = json.dump(new_data,data_file,indent=4)
            else:
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ----------------------------- Search -------------------------------- #

def search():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email":email,
            "password":password
        }
    }

    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="There is currently no data matching your search")
    else:
        if website in data:
            messagebox.showinfo(title=website,message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Data not found",message="The item you are searching for does not exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

#Displaying the Logo as a Canvas
image_logo = PhotoImage(file="logo.png")
logo_thing = Canvas(width=200,height=200)
logo_thing.create_image(100,100,image=image_logo)
logo_thing.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(row=2,column=1,columnspan=3)
email_entry.insert(END,"angela@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password",width=15,command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=45,command=save_user_info)
add_button.grid(row=4,column=1,columnspan=3)

search_button = Button(text="Search",width=15,command=search)
search_button.grid(row=1,column=2)






window.mainloop()
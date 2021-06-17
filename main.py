from tkinter import *
from tkinter import filedialog
from emailing import set_credentials, mail_sending
from tkinter import messagebox
from database import *



FILE_PATH = "/"



# ---------------------------- INITIATING MAIL SENDING ------------------------------- #

def boom():
    mail_sending(str(csv.name), str(file.name))
    messagebox.showinfo(title="Completed", message="All Mails are sent!!")
    a = get_query()
    for i in a:
        print(list(i))
    return


# ----------------------------SETS SENDER'S EMAIL AND PASS AND CALL BOOM------------------------------- #

def send_stuff():
    set_credentials(name_var.get(), passw_var.get())
    boom()
    name_var.set("")
    passw_var.set("")

# ---------------------------- ADD RECIPIENT ------------------------------- #

def add_recipient():
    input_(mail_entry.get(), passw_entry.get(), dob_entry.get())


# ---------------------------- DELETE RECIPIENT ------------------------------- #

def delete_recipient():
    delete_(pass_entry.get(), "Email")


# ---------------------------- SELECTS PDF ------------------------------- #

def file_opener():
    global file
    file = filedialog.askopenfile(initialdir=FILE_PATH, mode='r',
                                  title="Select a File",
                                  filetypes=(("pdf",
                                              "*.pdf"),
                                             ("Text files",
                                              "*.txt*"),
                                             ("all files",
                                              "*.*"),
                                             ("csv",
                                              "*.csv*")))
    isok = messagebox.askokcancel(title="Selected PDF",
                                  message=f"This is the chosen file: \n{file.name}\n\n Is it okay?\n ")
    if isok:
        Label(window, text=file.name.split('/')[-1], fg='green', bg='white').grid(row=6, column=2, padx=10, pady=10)
    else:
        file_opener()


# ---------------------------- SELECTS LIST OF RECIPIENTS ------------------------------- #

def csv_opener():
    global csv
    csv = filedialog.askopenfile(initialdir=FILE_PATH, mode='r', title="Select a File",
                                 filetypes=(("csv",
                                             "*.csv*"),
                                            ("pdf",
                                             "*.pdf"),
                                            ("Text files",
                                             "*.txt*"),
                                            ("all files",
                                             "*.*")
                                            ))
    isok = messagebox.askokcancel(title="Selected CSV",
                                  message=f"This is the chosen file: \n{csv.name}\n\n Is it okay?\n ")
    if isok:
        Label(window, text=csv.name.split('/')[-1], fg='green', bg='white').grid(row=8, column=2, padx=10, pady=10)
    else:
        csv_opener()


# ---------------------------- Senders UI SETUP------------------------------- #


window = Tk()
name_var = StringVar()
passw_var = StringVar()
window.title("MASS MAILING")
window.config(padx=75, pady=50, bg="white")

# CANVAS (IMAGE)
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(152, 100, image=logo_img)
canvas.grid(row=0, column=2)

# LABELS
website_label = Label(text="Enter SENDER'S CRED", bg="white", font=("Arial", 12))
website_label.grid(row=1, column=2)
username_label = Label(text="Email:", bg="white", font=("Arial", 12))
username_label.grid(row=2, column=1)
password_label = Label(text="Password:", bg="white", font=("Arial", 12))
password_label.grid(row=3, column=1)
Label(window, text="File_pdf", bg='white', font=('Arial', 12)).grid(row=4, column=2)
Label(window, text="File_csv", bg='white', font=('Arial', 12)).grid(row=6, column=2)
Label(window, bg='white').grid(row=8, column=2)
Label(window, bg='white').grid(row=4, column=2)

# ENTRY
username_entry = Entry(width=35, textvariable=name_var)
username_entry.focus()
username_entry.grid(row=2, column=1, columnspan=3)
pass_entry = Entry(text="", width=35, textvariable=passw_var, show='*')
pass_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# BUTTON
add_button = Button(text='Send', width=20, font=("Arial", 10), bg="white", command=send_stuff)
add_button.grid(row=9, column=1, columnspan=3)
b1 = Button(window, text='Browse', font=("Arial", 10), command=file_opener).grid(row=5, column=2)
b2 = Button(window, text='Browse', font=("Arial", 10), command=csv_opener).grid(row=7, column=2)

# ---------------------------- ADD RECIPIENT UI SETUP------------------------------- #


# LABELS
Label(window, bg='white').grid(row=10, column=1)
add_details_label = Label(text="Add Recipient:", bg="white", font=("Arial", 12))
add_details_label.grid(row=11, column=1, padx=10, pady=10)
name_label = Label(text="Name:", bg="white", font=("Arial", 12))
name_label.grid(row=12, column=0)
email_label = Label(text="Email:", bg="white", font=("Arial", 12))
email_label.grid(row=13, column=0)
dob_label = Label(text="DOB:", bg="white", font=("Arial", 12))
dob_label.grid(row=14, column=0)

# ENTRY

mail_entry = Entry(width=35)
mail_entry.grid(row=12, column=1)
passw_entry = Entry(text="", width=35)
passw_entry.grid(row=13, column=1)
dob_entry = Entry(width=35)
dob_entry.grid(row=14, column=1)

# BUTTON

add_button = Button(text='ADD', width=15, font=("Arial", 10), bg="white", command = add_recipient)
add_button.grid(row=15, column=1)

# ---------------------------- DELETE RECIPIENT UI SETUP------------------------------- #


# LABELS
Label(window, bg='white').grid(row=10, column=1)
del_details_label = Label(text="Delete Recipient:", bg="white", font=("Arial", 12))
del_details_label.grid(row=11, column=3, padx=10, pady=10)
n_label = Label(text="Name:", bg="white", font=("Arial", 12))
n_label.grid(row=12, column=2)
e_label = Label(text="Email:", bg="white", font=("Arial", 12))
e_label.grid(row=13, column=2)
del_dob_label = Label(text="DOB:", bg="white", font=("Arial", 12))
del_dob_label.grid(row=14, column=2)

# ENTRY

username_entry = Entry(width=35)
username_entry.grid(row=12, column=3)
pass_entry = Entry(text="", width=35)
pass_entry.grid(row=13, column=3)
DOB_entry = Entry(width=35)
DOB_entry.grid(row=14, column=3)

# BUTTON

DEL_button = Button(text='DELETE', width=15, font=("Arial", 10), bg="white", command = delete_recipient)
DEL_button.grid(row=15, column=3)

window.mainloop()

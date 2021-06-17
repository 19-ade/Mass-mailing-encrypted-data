from tkinter import *
from tkinter import filedialog
from email_try import set_credentials, mail_sending
from tkinter import messagebox

#FILE_PATH = "C:/Users/adity/Desktop/New folder/PYTHON PROJECTS/Mass Mailing/"


# ---------------------------- INITIATING MAIL SENDING ------------------------------- #

def boom():
    mail_sending(str(csv.name), str(file.name))
    messagebox.showinfo(title="Completed", message="All Mails are sent!!")
    return


# ----------------------------SETS SENDER'S EMAIL AND PASS AND CALL BOOM------------------------------- #

def send_stuff():
    set_credentials(name_var.get(), passw_var.get())
    boom()
    name_var.set("")
    passw_var.set("")


# ---------------------------- SELECTS PDF ------------------------------- #

def file_opener():

    global file
    file = filedialog.askopenfile(initialdir="/", mode='r',
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
        Label(window, text=file.name.split('/')[-1], fg = 'green', bg = 'white' ).grid(row=6, column=1, padx =10 , pady = 10)
    else:
        file_opener()
# ---------------------------- SELECTS LIST OF RECIPIENTS ------------------------------- #

def csv_opener():
    global csv
    csv = filedialog.askopenfile(initialdir="/", mode='r', title="Select a File",
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
        Label(window, text=csv.name.split('/')[-1], fg='green', bg='white').grid(row=8, column=1, padx=10, pady=10)
    else:
        csv_opener()
        
        
# ---------------------------- UI SETUP------------------------------- #

window = Tk()
name_var = StringVar()
passw_var = StringVar()
window.title("MASS MAILING")
window.config(padx=75, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(152, 100, image=logo_img)
canvas.grid(row=0, column=1)


# LABELS
website_label = Label(text="Enter credentials from which you want to send mails", bg="white", font=("Arial", 12))
website_label.grid(row=1, column=1)
username_label = Label(text="Email:", bg="white", font=("Arial", 12))
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white", font=("Arial", 12))
password_label.grid(row=3, column=0)
Label(window, text="File_pdf", bg='white', font=('Arial', 12)).grid(row=4, column=1)
Label(window, text="File_csv", bg='white', font=('Arial', 12)).grid(row=6, column=1)
Label(window, bg='white').grid(row=8, column=1)
Label(window, bg='white').grid(row=4, column=1)


# ENTRY
username_entry = Entry(width=35, textvariable=name_var)
username_entry.focus()
username_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(text="", width=35, textvariable=passw_var, show='*')
pass_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)


# BUTTON
add_button = Button(text='Send', width=20, font=("Arial", 10), bg="white", command=send_stuff)
add_button.grid(row=9, column=1, columnspan=2)
Button(window, text='Browse', font=("Arial", 10), command=file_opener).grid(row=5, column=1)
Button(window, text='Browse', font=("Arial", 10), command=csv_opener).grid(row=7, column=1)


window.mainloop()

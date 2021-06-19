# Mass-mailing-encrypted-data
Mass Mailing personalised encrypted files(pdfs) with personalised mail using SQLlite database. This mass-mailing application can send an encrypted PDF to the recipients. The password is set as default to be the Datae of Birth . However it can be changed . A basic database is included . The database can be manipulated by modifying the functions given in database_manage.py. The Database contains Name, Email and DOB columns. the program extracts the DOB and Email from this table. 

## Setting up the enviroment
------------------------------------------------------------------------

1. Clone the Mass-mailing-encrypted-data repo

```
git clone https://github.com/19-ade/Mass-mailing-encrypted-data.git
```
Navigate your way to the Mass mailing encrypted data folder. 

2. Run Requirements.py

```
python Requirements.py
```

3. Run the GUI 

```
python main.py
```

## Description of the Scripts
-----------------------------------------------------------------------

1.**email_try.py** : This is the script which performs the encryption and sends the mails. **make_pdf** encrypts the pdf. **send_mail** sends the mails ; the contents of the mail text can be manipulated here . **mail_sending** recieves the inputs from various scripts and calls the aforementioned functions. **set_credentials** recieves the sender's email id and password from the gui and initialises the global variables email and password with it .

2.**main.py** : This is GUI interface for the project . Made with tkinter. 

3.**database_manage.py** : This contains various functions which can help manipulate the basic layout of the database, mass_mailing.db. Made with sqlite3

4.**csv_creator**: Creates , edits the csv files containing the mailing list. The functionalities will be added with further updates. 


## A visual 
-------------------------------------------------------------------------


![Screenshot from 2021-06-18 16-06-10](https://user-images.githubusercontent.com/64825911/122551877-31205e80-d053-11eb-8651-06ec8c83d977.png)
                                                         **The Outlay of our GUI**

![Screenshot from 2021-06-18 16-08-41](https://user-images.githubusercontent.com/64825911/122552095-7d6b9e80-d053-11eb-806f-5b9c1a1b1cef.png)

**Inputs for appending to the Database**

![Screenshot from 2021-06-18 16-07-24](https://user-images.githubusercontent.com/64825911/122552043-6cbb2880-d053-11eb-8007-83ace008b4de.png)

**messagebox confirming the pdf to be uploaded**

![Screenshot from 2021-06-18 16-09-02](https://user-images.githubusercontent.com/64825911/122552207-a1c77b00-d053-11eb-8b6a-d0a15726abcc.png)

**Messagebox confirmation feature**

![Screenshot from 2021-06-18 16-10-03](https://user-images.githubusercontent.com/64825911/122552242-ae4bd380-d053-11eb-9197-e5169634cf0d.png)

**Deleting from the Database with just the email. More fetures will be added**

![Screenshot from 2021-06-18 16-11-36](https://user-images.githubusercontent.com/64825911/122552315-c7ed1b00-d053-11eb-9188-454f788bd75e.png)

**Confirmation messagebox on successfully sending all the mails**



## Updates
---------------------------------------------------------------------------
- error message functionality for wrong entries while deleting and pressing delete without any inputs added
- Deleting a record can now be achieved with entering any one of the values (Email, dob, name) or all of them 
- New button features added which allows users to directly download the database contents in either excel or csv file .




## Appreciation
---------------------------------------------------------------------------

The project would not have been possible without contributions from [Aditya Goyal](https://github.com/adigo12), [Nirav Jayesh Parmar](https://github.com/Nirav0702). Made with love,  in Python .

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from PyPDF2 import PdfFileWriter, PdfFileReader


def set_credentials(e, p):
    global email, password
    email = e
    password = p


def make_pdf(file, password):
    out = PdfFileWriter()
    num = file.numPages
    for i in range(num):
        page = file.getPage(i)
        out.addPage(page)
    passw = password
    out.encrypt(passw)
    with open("Encrypted_pdf.pdf", "wb") as f:
        out.write(f)


def send_mail(i):
    mail_content = "Hello, " + i[0] + "\n The password is your name DOB"
    sender_address = email
    sender_pass = password
    receiver_address = i[1]
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Open me pls'

    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'Encrypted_pdf.pdf'
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent to ' + i[0])


def mail_sending(datab, file_path):
    file = PdfFileReader(file_path)
    df = datab
    for i in df:
        make_pdf(file, str(i[2]))
        send_mail(i)

from tkinter import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#GUI
def sent():
    global alamat_email, password, subject, pesan
    alamat_email = str(e1.get())
    password = str(e2.get())
    subject = str(e3.get())
    pesan = str(T.get("1.0",END))
    # print(alamat_email)
    # print(password)
    # print(subject)
    # print(pesan)
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email import encoders

    alamatemailnya = []
    listalamatemail = []
    file = open("alamat_email.txt", "r")
    for nama in file:
        alamatemailnya.append(nama)

    for nama in alamatemailnya:
        listkatahapus = nama.replace("\n","")
        listalamatemail.append(listkatahapus)

    #Sender, Reciever, Body of Email
    sender = alamat_email
    receivers = listalamatemail
    body_of_email = pesan

    #Creating the Message, Subject line, From and To
    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    #Connecting to Gmail SMTP Server
    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = sender, password = password)
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()

def keluar():
    exit()

#userinterface
ui=Tk()
ui.title('Email Messenger Indonesian.ai Batch 4') 
ui.geometry("400x400")

l1 = Label(ui, text='Enter Your Email :').grid(row=0, pady=5) 
l2 = Label(ui, text='Enter Your Password :').grid(row=1, pady=5)
l3 = Label(ui, text='Enter Your Subject :').grid(row=2, pady=5) 

e1 = Entry(ui, width=40) 
e1.grid(row=0, column=1, pady=5)
e2 = Entry(ui, width=40) 
e2.grid(row=1, column=1, pady=5) 
e3 = Entry(ui, width=40) 
e3.grid(row=2, column=1, pady=5) 

l4 = Label(ui, text="Your Message :").grid(row=3)
T = Text(ui, height=10, width=30) 
T.insert(END,"") 
T.grid(row=3, column=1, pady=5)

b1 = Button(ui, text='Sent', width=10, command=sent, bg='white') 
b1.grid(row=4, column=0, pady=10)
b2 = Button(ui, text='Exit', width=10, command=keluar, bg='white') 
b2.grid(row=5, column=0, pady=10)
ui.mainloop()

'''
Referensi
https://www.youtube.com/watch?v=iICg4Vn2Rkk
https://nitratine.net/blog/post/how-to-send-an-email-with-python/
https://github.com/python/cpython/blob/3.9/Lib/smtplib.py
https://www.geeksforgeeks.org/python-gui-tkinter/#:~:text=Python%20offers%20multiple%20options%20for,to%20create%20the%20GUI%20applications.
'''
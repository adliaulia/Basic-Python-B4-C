#Importing Packages
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
sender = 'alamatemailpengirim@gmail.com'
receivers = listalamatemail
body_of_email = 'Pesan dalam email'

#Creating the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Subject untuk email'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Adds a csv file as an attachment to the email 
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Users/adli/namafilenya.extensionfile', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="namafilenya.extensionfile"')
msg.attach(part)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = 'passwordgmailpengirim')
s.sendmail(sender, receivers, msg.as_string())
s.quit()

'''
Referensi
https://www.youtube.com/watch?v=iICg4Vn2Rkk
https://nitratine.net/blog/post/how-to-send-an-email-with-python/
https://github.com/python/cpython/blob/3.9/Lib/smtplib.py
https://www.geeksforgeeks.org/python-gui-tkinter/#:~:text=Python%20offers%20multiple%20options%20for,to%20create%20the%20GUI%20applications.
'''
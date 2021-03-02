import  tkinter as tk
from tkinter import filedialog
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master = master
        self.title = master.title
        self.geometry = master.geometry
        self.title('Email Messenger Indonesian.ai Batch 4') 
        self.geometry("400x450")
        self.create_widgets()
        self.grid()
    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there = ['text'] = 'Hello World, \n(click me)'
        # self.hi_there['command'] = self.say_hi
        # self.hi_there.grid(row=0)
        self.l1 = tk.Label(self, text='Enter Your Email :').grid(row=0, pady=5) 
        self.l2 = tk.Label(self, text='Enter Your Password :').grid(row=1, pady=5)
        self.l3 = tk.Label(self, text='Enter Your Subject :').grid(row=2, pady=5) 
        self.e1 = tk.Entry(self, width=40)
        self.e1.grid(row=0, column=1, pady=5)
        self.e2 = tk.Entry(self, width=40) 
        self.e2.grid(row=1, column=1, pady=5) 
        self.e3 = tk.Entry(self, width=40) 
        self.e3.grid(row=2, column=1, pady=5) 
        self.l4 = tk.Label(self, text="Your Message :").grid(row=3)
        self.T = tk.Text(self, height=10, width=30) 
        self.T.insert('1.0','') 
        self.T.grid(row=3, column=1, pady=5)
        self.browsebutton = tk.Button(self, width=10, text="Browse", command=self.locfile)
        self.browsebutton.grid(row=4, column=1, pady=5)
        self.pathlabel = tk.Label(self)
        self.pathlabel.grid(row=5, column=1, pady=5)
        self.l5 = tk.Label(self, text="filename :").grid(row=6)
        self.e4 = tk.Entry(self, width=40) 
        self.e4.grid(row=6, column=1, pady=5) 
        self.b1 = tk.Button(self, text='Sent', width=10, command=self.sent, bg='white') 
        self.b1.grid(row=7, column=0, pady=5)
        self.b2 = tk.Button(self, text='Exit', width=10, command=self.keluar, bg='white') 
        self.b2.grid(row=8, column=0, pady=5)
        # self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
        # self.quit.grid(row=3)
    def components(self):
        self.your_email = str(self.e1.get())
        self.password = str(self.e2.get())
        self.subject = str(self.e3.get())
        self.pesan = str(self.T.get('1.0','END'))
        print(self.your_email)
        return self.your_email, self.password, self.subject, self.pesan
    def locfile(self):
        self.locfilenames = filedialog.askopenfilename(filetypes=[("all files", "*")])
        self.namafiles = str(self.e4.get())
        self.pathlabel.config(text=self.locfilenames)
        print(self.locfilenames)
        return self.locfilenames, self.namafiles
    def keluar(self):
        exit()
    def sent(self):
        a=self.components()
        print(a)

    # def say_hi(self):
    #     print('Hi Everyone')

root = tk.Tk()
app = Application(master=root)
app.mainloop()

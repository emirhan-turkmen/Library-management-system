from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
import sys
py=sys.executable


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("KUTUPHANE YONETIM SISTEMI")


#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" hatali kullanici adi veya sifre" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" hatali kullanici adi veya sifre")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Hata', 'Kullanıcı Adı veya Şifre Yanlış')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Hata',"Bir şeyler ters gitti, Lütfen tekrar deneyin")

        def check():


                    self.label = Label(self, text="Giris", bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
                    self.label.place(x=550, y=90)
                    self.label1 = Label(self, text=" Kullanıcı Adı:" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=300, y=180)
                    self.user_text = Entry(self, textvariable=self.a, width=45)
                    self.user_text.place(x=480, y=190)
                    self.label2 = Label(self, text=" Şifre:" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=300, y=250)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
                    self.pass_text.place(x=480, y=255)
                    self.butt = Button(self, text="Giris",bg ='white', font=10, width=8, command=chex).place(x=560, y=300)
                    self.label3 = Label(self, text="    Kutuphane Yonetim Sistemi", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
                    self.label3.place(x=350, y=30)


        check()

Lib().mainloop()
from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Kul. Ekle')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "Kullanici Eklendi")
                ask = messagebox.askyesno("Confirm", "Baska kullanici eklemek ister misiniz")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Hata", "Bir şeyler ters gitti")
#label and input
        Label(self, text='Kullanıcı Detayları:', bg='gray', fg='black', font=('Courier new', 25, 'bold')).place(x=50, y=22)
        Label(self, text='Kul. Adi:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='İsim:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Sifre:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Kaydet", width=15, command=insert).place(x=230, y=220)
reg().mainloop()
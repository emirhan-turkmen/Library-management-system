from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('KITAP EKLE')
        self.canvas = Canvas(width=500, height=500, bg='gray')
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        #verifying Input
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("HATA","Lütfen detaylari girin")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",[b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Bilgi', 'Basariyla Eklendi')
                    ask = messagebox.askyesno("Confirm", "Baska bir kitap eklenecek mi?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Hata","Detaylari kontrol edin")
        #creating input box and label
        Label(self, text='').pack()
        Label(self, text='Kitap Detaylari:',bg='gray',fg='black',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Kitap Adi:',bg='gray',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='Yazar:',bg='gray',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=c, width=30).place(x=170, y=232)
        Button(self, text="Kaydet", command=b_q).place(x=245, y=300)
Add().mainloop()
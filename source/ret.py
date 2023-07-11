from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("Iade")
        self.maxsize(420,280)
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Lutfen kitap ID girin")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='testdb3',
                                                        user='root',
                                                        password='1')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Iade edildi')
                        d = messagebox.askyesno("Confirm", "Iade edilecek baska kitap var mi?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Kitap henuz odunc alınmadı")
                except Error:
                    messagebox.showerror("Error","Bir şeyler ters gitti")
        Label(self, text='').pack()
        Label(self, text='Iade Et', fg='black',font=('Comic Scan Ms', 15, 'bold')).place(x=170, y=60)
        Label(self, text='Kitap ID', font=('Comic Scan Ms', 15, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=a, width=40).place(x=165, y=124)
        Button(self, text="Tamamla", width=25, command=qui).place(x=180, y=180)
ret().mainloop()
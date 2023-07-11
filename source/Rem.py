from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Kullanici Silme")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Hata","Lutfen var olan bir ID girin")
            else:
                d = messagebox.askyesno("Confirm", "Baska bir kullanici silmek ister misiniz")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","Kullanici silindi")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Bir şeyler ters gitti")
        Label(self, text = " Kullanici ID ",bg='gray',fg='black',font=('Courier new', 15, 'bold')).place(x = -7,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Sil', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()
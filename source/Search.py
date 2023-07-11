from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Kitap Ara")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='gray')
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        l1=Label(self,text="Kutuphanede Ara",bg='gray', font=("Courier new",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Kriter",bg='gray', font=("Courier new", 15, 'bold')).place(x=80, y=96)
        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'Önce Kriter secin')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Girin '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Kitap Adi hatali yada kitap musait degil")
                except Error:
                    messagebox.showerror("Error","Bir şeyler ters gitti")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where author LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Yazar bulunamadı")
                except Error:
                    messagebox.showerror("Error","bir şeyler ters gitti")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='testdb3',
                                         user='root',
                                         password='1')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Kitap Adi hatali yada kitap musait degil")
                except Error:
                    messagebox.showerror("Error","Bir şeyler ters gitti")
        b=Button(self,text="Bul",width=15,bg='gray',font=("Courier new",10,'bold'),command=ge).place(x=460,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["Book Name","Author Name","Book Id"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Girin",bg='gray', font=("Courier new", 15, 'bold')).place(x=80, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Kitap ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Kitap Adi')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Yazar')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Durum')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Search().mainloop()
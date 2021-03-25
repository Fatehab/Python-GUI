import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


class Window1:
    def __init__(self, master):
        # creating window
        self.master = master
        self.master.title("AAT Admin")
        self.master.config(bg='floral white')
        # adding a icon photo to the gui
        self.master.iconphoto(True, tk.PhotoImage(file='diamond.png'))
        # setting size when window is displayed
        self.master.geometry('600x600')
        # creating my main frame inside window which will have other frames inside
        self.m_frame = Frame(self.master, bg='bisque', bd=5, relief=RIDGE, width=70, height=100)
        self.m_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.Username = StringVar()
        self.Password = StringVar()

        # Label for username and password and textboxes
        self.lbl1 = tk.Label(self.m_frame, text='Username', bg='bisque')
        self.lbl1.pack(pady=20)
        self.textbox1 = tk.Entry(self.m_frame, width=35)
        self.textbox1.pack(pady=20)
        self.lbl2 = tk.Label(self.m_frame, text='Password', bg='bisque')
        self.lbl_font = font.Font(family='Georgia', size='20', weight='bold')
        self.lbl2.pack(pady=20)
        self.textbox2 = tk.Entry(self.m_frame, width=35, show="*")
        self.textbox2.pack(pady=10)
        self.login1 = tk.Button(self.m_frame, text="Sign in", fg='black', bg='white', cursor='arrow',
                                command=self.logins)
        self.login1.pack(pady=50, padx=30)
        self.delete2 = tk.Button(self.m_frame, text='Delete', fg='black', bg='white', command=self.delete)
        self.delete2.pack()

    # function for clearing textbox
    def delete(self):
        self.textbox1.delete(0, END)
        self.textbox2.delete(0, END)

    # function for user and password validation
    def logins(self):
        user = (self.textbox1.get())
        passw = (self.textbox2.get())

        if user == 'Fateha' or 'Fahim' and passw == 'Cat':
            self.newwindow = Toplevel(self.master)
            self.app = Window2(self.newwindow)

        else:
            messagebox.showinfo("AAT", "Incorrect Username and Password")

    # defining new window for after login
    def window22(self):
     self.newwindow = Toplevel(self.master)
     self.app = Window2(self.newwindow)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("AAT Admin SQL Database")

        # setting size for the window when displayed
        self.master.geometry('900x700')

        # icon photo for the window
        self.master.iconphoto(True, tk.PhotoImage(file='diamond.png'))
        # background colour for the window
        self.master.config(bg='floral white')
        # db frame is the mainframe for the window which has other frames
        self.db_frame = Frame(self.master, bg='bisque', bd=5, relief=RIDGE, width=800, height=800)
        self.db_frame.pack(fill="both", expand=True, padx=15, pady=15)
        # labels frame is for the tree view,add,edit and delete
        self.labels_frame = Frame(self.db_frame, bg='white', bd=2, relief=RIDGE, width=700, height=700)
        self.labels_frame.pack(side=RIGHT, padx=0, pady=0, expand=True)

        # variables for entry boxes for when administrators add edit delete database with entry boxes
        self.cid = StringVar()
        self.cat = StringVar()
        self.prod = StringVar()
        self.name = StringVar()
        self.stock = StringVar()
        self.price = StringVar()
        self.data1 = StringVar()
        self.data2 = StringVar()
        self.data3 = StringVar()
        self.data4 = StringVar()
        self.data5 = StringVar()
        self.data6 = StringVar()

        # tree view to display the table information in the gui just like it would in mysql database
        self.tree = ttk.Treeview(self.labels_frame)
        self.tree['columns'] = ('Category ID', 'Category Name', 'Product ID', 'Product Name', 'Stock', 'Price')
        self.tree.place(x=50, y=410)
        self.tree.heading('Category ID', text='Category ID')
        self.tree.column('Category ID', width='80', minwidth=80, stretch=FALSE)
        self.tree.heading('Category Name', text='Category Name')
        self.tree.column('Category Name', width='80', minwidth=80, stretch=FALSE)
        self.tree.heading('Product ID', text='Product ID')
        self.tree.column('Product ID', width='80', minwidth=80, stretch=FALSE)
        self.tree.heading('Product Name', text='Product Name')
        self.tree.column('Product Name', width='80', minwidth=80, stretch=FALSE)
        self.tree.heading('Stock', text='Stock')
        self.tree.column('Stock', width='40', minwidth=80, stretch=FALSE)
        self.tree.heading('Price', text='Price')
        self.tree.column('Price', width='40', minwidth=80, stretch=FALSE)

        # creating labels and entry boxes
        l1 = Label(self.labels_frame, text='Category Code', width=12, bg='white')
        l1.place(x=50, y=60)
        self.e1 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.cid)
        self.e1.place(x=170, y=60)
        l2 = Label(self.labels_frame, text='Category Name', width=12, bg='white')
        l2.place(x=50, y=100)
        self.e2 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.cat)
        self.e2.place(x=170, y=100)
        l3 = Label(self.labels_frame, text='Product Code', width=12, bg='white')
        l3.place(x=50, y=140)
        self.e3 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.prod)
        self.e3.place(x=170, y=140)
        l4 = Label(self.labels_frame, text='Product Name', width=12, bg='white')
        l4.place(x=50, y=180)
        self.e4 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.name)
        self.e4.place(x=170, y=180)
        l5 = Label(self.labels_frame, text='Stock', width=12, bg='white')
        l5.place(x=50, y=220)
        self.e5 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.stock)
        self.e5.place(x=170, y=220)
        l6 = Label(self.labels_frame, text='Price', width=12, bg='white')
        l6.place(x=50, y=260)
        self.e6 = Entry(self.labels_frame, width=30, bg='bisque', textvariable=self.price)
        self.e6.place(x=170, y=260)
        # button for the add edit delete clear save&print
        self.view = Button(self.labels_frame, text='VIEW DATA', width=20, bg='bisque', command=self.display_action)
        self.view.place(x=400, y=50)
        self.add = Button(self.labels_frame, text='ADD', width=20, bg='bisque', command=self.test)
        self.add.place(x=400, y=90)
        self.edit1 = Button(self.labels_frame, text='SELECT RECORD', width=20, bg='bisque')
        self.edit1.place(x=400, y=130)
        self.edit2 = Button(self.labels_frame, text='UPDATE', width=20, bg='bisque', command=self.update)
        self.edit2.place(x=400, y=170)
        self.delete = Button(self.labels_frame, text='DELETE', width=20, bg='bisque', command=self.delete3)
        self.delete.place(x=400, y=210)
        self.clearing = Button(self.labels_frame, text='CLEAR', width=20, bg='bisque', command=self.clear)
        self.clearing.place(x=400, y=250)
        self.stocktaking = Button(self.labels_frame, text='PERFORM STOCK TAKING', width=20, bg='bisque',
                                  command=self.file)
        self.stocktaking.place(x=400, y=290)

        # this frame is for performing stock taking
        self.file = Frame(self.master, bg='bisque', bd=5, relief=RIDGE, width=800, height=800)
        # textbox for file and saving with data from table with date and time in filename
        self.text = Text(self.file, bd=5, relief=RIDGE, width=100, height=20)
        self.text.place(x=10, y=30)

        # button for inserting a file to the textbox so i can edit & perform stock taking
        open_button = Button(self.file, text='Insert to textbox', width=25, bg='white', command=self.open_txt)
        open_button.place(x=900, y=100)

        # button to extract table data of ProductS to the textbox so it can be saved and printed
        extract_button = Button(self.file, text='Extract from table', width=25, bg='white', command=self.extract_data)
        extract_button.place(x=900, y=150)

        # button for extracting products low in stock to the textbox so it can be saved to a file & printed
        low_stock_button = Button(self.file, text='Insert low stock items', width=25, bg='white',
                                  command=self.low_stock)
        low_stock_button.place(x=900, y=200)

        # button to save the file which the file name can be edited and you can save the file as all files or text file
        save_button = Button(self.file, text='Save&Print', width=25, bg='white', command=self.save_file)
        save_button.place(x=900, y=250)

        # button lets you go back to the second frame
        button = Button(self.file, text='Back To Database Page', width=25, bg='white', command=self.back)
        button.place(x=900, y=300)

    # this function is for saving the file stock taking and choosing a file type
    def save_file(self):
        file = filedialog.asksaveasfile(initialdir="2021CW", defaultextension='.txt',
                                        filetypes=[("Text File", ".txt"),
                                                   ("All files", ".*")])
        filetext = str(self.text.get(1.0, END))
        file.write(filetext)
        file.close()

    # this function is for user to open a file and editing it with textbox and adding new data from database
    def open_txt(self):
        text_file = filedialog.askopenfilename(initialdir="C:/56/", title="Open Text File", filetypes=(("Text Files",
                                               '*.txt'),))
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        self.text.insert(END, stuff)
        text_file.close()

    # this function allows user to go to the second frame and edit database table
    def back(self):
        self.file.forget()
        self.db_frame.pack()

    # this function allows user to go to the stock taking frame
    def file(self):
        self.db_frame.forget()
        self.file.pack(fill="both", expand=True, padx=15, pady=15)

    # this function is for the entry boxes text variables
    def test(self):
        self.insert(self.cid.get(), self.cat.get(), self.prod.get(), self.name.get(),
                    self.stock.get(), self.price.get())

    # this function is for adding data to the database
    def insert(self, cid, cat, prod, name, stock, price):
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO toy (id,cat,productID,name,stock,price) VALUES(?,?,?,?,?,?)",
                       (cid, cat, prod, name, stock, price))
        connection.commit()

        connection.close()

    # this function is for deleting data from the database
    def delete3(self):
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        for treeview in self.tree.selection():
            cursor.execute('DELETE FROM toy WHERE (id=?)', (self.tree.set(treeview, '#1'),))
            self.tree.delete(treeview)
        connection.commit()
        connection.close()

    # this function is for editing the database
    def update(self):
       self.data2 = self.cat.get()
       self.data3 = self.prod.get()
       self.data4 = self.name.get()
       self.data5 = self.stock.get()
       self.data6 = self.price.get()
       print(self.tree.selection())
       for selected in self.tree.selection():
        self.e1.insert(0, selected)
        self.e2.insert(0, selected)
        self.e3.insert(0, selected)
        self.e4.insert(0, selected)
        self.e5.insert(0, selected)
        self.e6.insert(0, selected)
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE toy SET cat=?,productID=?,name=?,stock=?,price=? WHERE id =?", (self.data2, self.data3,
                                                     self.data4, self.data5, self.data6, self.tree.set(selected, '#1')))
        connection.commit()
        connection.close()

    # this function is for selecting the tree view row and it will insert it in the entry box
    def get_selected_row(self):
      print(self.tree.selection())
      for nm in self.tree.selection():
       content = self.tree.item(nm, 'values')
       self.e1.insert(END, content[1])
       self.e2.insert(END, content[2])
       self.e3.insert(END, content[3])
       self.e4.insert(END, content[4])
       self.e5.insert(END, content[5])
       self.e6.insert(END, content[6])

    # this function is for getting all the data from the toy table into the tree view
    def display(self):
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        rows = cursor.execute("SELECT id,cat,productID,name,stock,price FROM toy").fetchall()
        return rows

    # this function is linked to display query function and inserts all the information into the tree view
    def display_action(self):
        rows = self.display()
        for ro in rows:
         self.tree.insert('', END, values=ro)

    # this function is for clearing the entry boxes to make it quicker for user to add data & clear it for the new input
    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)

    # this function is for taking all the data from the table toy and putting it in the textbox for stock taking
    def extract_data(self):
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM toy")
        list0 = cursor.fetchall()
        cursor.close()
        output = ''
        for x in list0:
            self.text.insert(END, f"{x}\n")
        return output

    # this function is for extracting data that is low stock items and inputting it into the textbox for stock taking
    def low_stock(self):
        connection = sqlite3.connect("sql.db")
        cursor = connection.cursor()
        cursor.execute("SELECT productID FROM toy WHERE stock < 20")
        items = cursor.fetchall()
        cursor.close()
        for x in items[0:10]:
         self.text.insert(END, f"{x}\n")
         print(x)

if __name__ == '__main__':
    master = tk.Tk()
    app = Window1(master)
    master.mainloop()
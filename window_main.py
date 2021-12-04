import tkinter as tk
from tkinter import ttk
from sql import return_records,name_company


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.tree = ttk.Treeview(self,columns=('supplier_id','company_name','contact_name' , 'contact_title' , 'address',
                                               'city', 'region' , 'postal_code','country', 'phone', 'fax'),
                                 height=30,show ='headings')

        self.tree.column('supplier_id', width=50, anchor=tk.CENTER)
        self.tree.column('company_name', width = 200, anchor = tk.CENTER)
        self.tree.column('contact_name', width=100, anchor=tk.CENTER)
        self.tree.column('contact_title', width=150, anchor=tk.CENTER)
        self.tree.column('address', width=150, anchor=tk.CENTER)
        self.tree.column('city', width=100, anchor=tk.CENTER)
        self.tree.column('region', width=100, anchor=tk.CENTER)
        self.tree.column('postal_code', width=100, anchor=tk.CENTER)
        self.tree.column('country', width=100, anchor=tk.CENTER)
        self.tree.column('phone', width=100, anchor=tk.CENTER)
        self.tree.column('fax', width=100, anchor=tk.CENTER)


        self.tree.heading('supplier_id', text='supplier_id')
        self.tree.heading('company_name', text='company_name')
        self.tree.heading('contact_name', text='contact_name')
        self.tree.heading('contact_title', text='contact_title')
        self.tree.heading('address', text='address')
        self.tree.heading('city', text='city')
        self.tree.heading('region', text='region')
        self.tree.heading('postal_code', text='postal_code')
        self.tree.heading('country', text='country')
        self.tree.heading('phone', text='phone')
        self.tree.heading('fax', text='fax')


        self.tree.pack()

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)


        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                               compound=tk.TOP, command = self.view_records)
        btn_refresh.pack(side=tk.LEFT)

    def open_search_dialog(self):
        Search()

    def view_records(self):
        self.date = return_records()
        for row in self.date:
            self.tree.insert('', tk.END, values=row)

    def search_records(self,description):
        date = name_company(description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end',values = row) for row in date]




class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False,False)

        label_search = tk.Label(self, text = 'Поиск')
        label_search.place(x=50,y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105,y=20, width = 150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(),add='+')


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Tinkoff")
    root.geometry("1300x650+300+200")
    root.resizable(False, False)
    root.mainloop()
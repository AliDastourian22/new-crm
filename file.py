#colorb-111111
#colorw-F5F5F5
from tkinter import *
from tkinter import ttk

root=Tk()

root.title('practice')

root.geometry('1000x500')
root.resizable(False,False)

style = ttk.Style()

style.theme_use('default')

style.configure('Treeview', background='#F5F5F5',
                foreground='#111111',
                rowheight=25, fieldbackground='#F5F5F5')

style.map('Treeview', background=[('selected', '#0000ff')])

tree_frame=Frame(root)
tree_frame.pack(pady=10)

tree_scroll= Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode='extended')
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("Firstname","Lastname","ID" , "City" , "Address" , "State" , "Zipcode")
my_tree.column("#0",width=0, stretch=NO)
my_tree.column("Firstname",width=140,anchor=W)
my_tree.column("Lastname",width=140,anchor=W)
my_tree.column("ID",width=140,anchor=CENTER)
my_tree.column("City",width=140,anchor=CENTER)
my_tree.column("State",width=140,anchor=CENTER)
my_tree.column("Zipcode",width=140,anchor=CENTER)






















root.mainloop()
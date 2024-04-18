
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

my_tree['columns'] = ("Firstname", "Lastname", "ID", "City", "Address", "State", "Zipcode")
my_tree.column("#0",width=0, stretch=NO)
my_tree.column("Firstname",width=140,anchor=W)
my_tree.column("Lastname",width=140,anchor=W)
my_tree.column("ID",width=140,anchor=CENTER)
my_tree.column("City",width=140,anchor=CENTER)
my_tree.column("State",width=140,anchor=CENTER)
my_tree.column("Zipcode",width=140,anchor=CENTER)
my_tree.column("Address",width=140,anchor=CENTER)

my_tree.heading("#0", anchor=W)
my_tree.heading("Firstname", anchor=W, text="Firstname")
my_tree.heading("Lastname", anchor=W, text="Lastname")
my_tree.heading("ID", anchor=CENTER, text="ID")
my_tree.heading("City", anchor=CENTER, text="Address")
my_tree.heading("State", anchor=CENTER, text="State")
my_tree.heading("Zipcode",anchor=CENTER, text="Zipcode")
my_tree.heading("Address",anchor=CENTER,text="City")

my_tree.tag_configure('oddrow' , background="#f5f5f5")
my_tree.tag_configure('evenrow' , background="#006A93")


data=[
	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]]

global count
count=0
for record in data:
    if count % 2 ==0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags='evenrow')
    else:
        my_tree.insert(parent='', index='end', iid=count, text='',
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                       tags='oddrow', )
    count += 1

data_frame=LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label=Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry=Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)






root.mainloop()
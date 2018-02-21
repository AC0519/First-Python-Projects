"""
A program that stores this book information:
location, Name, Year, Casenumber

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from backendPRcases import Database

database=Database()

def get_selected_row(location):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(location_text.get(), name_text.get(), year_text.get(), casenumber_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(location_text.get(), name_text.get(), year_text.get(), casenumber_text.get())
    list1.delete(0,END)
    list1.insert(END,(location_text.get(), name_text.get(), year_text.get(), casenumber_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],location_text.get(), name_text.get(), year_text.get(), casenumber_text.get())

window = Tk()

window.wm_title("PR Cases")

l1=Label(window, text = "Location")
l1.grid(row=0,column=0)

l2=Label(window, text = "Name")
l2.grid(row=0,column=2)

l3=Label(window, text = "Year")
l3.grid(row=1,column=0)

l4=Label(window, text = "Casenumber")
l4.grid(row=1,column=2)

location_text=StringVar()
e1=Entry(window, textvariable=location_text)
e1.grid(row=0,column=1)

name_text=StringVar()
e2=Entry(window, textvariable=name_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

casenumber_text=StringVar()
e4=Entry(window, textvariable=casenumber_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View all", width=15, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=15, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=15, command=add_command)
b3.grid(row=4, column=3)

b1=Button(window, text="Update", width=15,command=update_command)
b1.grid(row=5, column=3)

b1=Button(window, text="Delete", width=15, command=delete_command)
b1.grid(row=6, column=3)

b1=Button(window, text="Close", width=15,command=window.destroy)
b1.grid(row=7, column=3)

window.mainloop()

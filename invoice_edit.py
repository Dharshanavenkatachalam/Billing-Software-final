from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import time
from tkinter import messagebox
import mysql.connector as sql

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Invoice Edit - Ajra Tex")
tk.configure(bg='white')

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="ajra")
cursor=mycon.cursor()
edit_selected_item = ""

def clear_item():
    particulars_entry.delete(0,END)
    quantity_entry.delete(0,END)
    quantity_entry.insert(0, "0")
    price_entry.delete(0,END)
    price_entry.insert(0, "0.0")
    
invoice_list = []
def add_item():
    particulars = particulars_entry.get()
    quantity = int(quantity_entry.get())
    unit_price = float(price_entry.get())
    line_total = quantity*unit_price
    invoice_item = [particulars, quantity, unit_price, line_total]
    tree.insert('',0, values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item) 
    
    sub_total = sum(item[3] for item in invoice_list)
    stotal_entry.delete(0,END)
    stotal_entry.insert(0,sub_total)
    
    cgst_entry.delete(0,END)
    cgst_entry.insert(0,sub_total*0.09)
    
    sgst_entry.delete(0,END)
    sgst_entry.insert(0,sub_total*0.09)
    
    gtotal_entry.delete(0,END)
    gtotal_entry.insert(0,sub_total+sub_total*0.18)

def edit_invoice():
    inv_no = str(invoice_number_entry.get())
    show = ("SELECT * FROM invoice WHERE invoice_no = '{}'").format(inv_no)
    cursor.execute(show)
    data=cursor.fetchall()[0]
    
    name_entry.insert(0,data[3])
    address_entry.insert(0,data[4])
    phone_number_entry.insert(0,data[5])
    gst_entry.insert(0,data[6])
    
    stotal_entry.delete(0,END)
    stotal_entry.insert(0,data[11])
    cgst_entry.delete(0,END)
    cgst_entry.insert(0,data[12])
    sgst_entry.delete(0,END)
    sgst_entry.insert(0,data[13])
    gtotal_entry.delete(0,END)
    gtotal_entry.insert(0,data[14])
    
    particulars = data[7].split(',')
    quantity = data[8].split(',')
    unit_price = data[9].split(',')
    line_total = data[10].split(',')
    
    for i in range(len(particulars)):
        invoice_item = [particulars[i], int(quantity[i]), float(unit_price[i]), float(line_total[i])]
        tree.insert('',0, values=invoice_item)
        invoice_list.append(invoice_item)

def edit_selection():
   selected_item = tree.selection()[0]
   item = tree.item(selected_item)['values']
   
   particulars_entry.delete(0,END)
   particulars_entry.insert(0,item[0])
   quantity_entry.delete(0,END)
   quantity_entry.insert(0,int(item[1]))
   price_entry.delete(0,END)
   price_entry.insert(0,float(item[2]))
   
Label(tk,text="AJRA TEX - KARUR",font=("Arial", 20, "bold"),bg="white",fg="#1A374D").place(x=650,y=20)
Label(tk,text="Invoice Number : ",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=580,y=100)

invoice_number_entry = Entry(tk,font=("Arial", 12, "bold"),bd=3)
invoice_number_entry.place(x=730,y=100)

edit_button = Button(tk, text="Submit",font=("Arial", 10,"bold"),bg="#1A374D",fg="#F5F5F5",command=edit_invoice)
edit_button.place(x=930,y=97)

name_label = Label(tk, text="Name",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=260,y=150)
name_entry = Entry(tk,font=("Arial", 12),bd=3)
name_entry.place(x=190,y=180)

address_label = Label(tk, text="Address",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=560,y=150)
address_entry = Entry(tk,font=("Arial", 12),bd=3)
address_entry.place(x=500,y=180)

phone_number_label = Label(tk, text="Phone number",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=850,y=150)
phone_number_entry = Entry(tk,font=("Arial", 12),bd=3)
phone_number_entry.place(x=810,y=180)

gst_label = Label(tk, text="GST number",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=1160,y=150)
gst_entry = Entry(tk,font=("Arial", 12),bd=3)
gst_entry.place(x=1110,y=180)

'''------- Product details -------'''

particulars_label = Label(tk, text="Particulars",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=240,y=230)
particulars_entry = Entry(tk,font=("Arial", 12),bd=3)
particulars_entry.place(x=190,y=260)

quantity_label = Label(tk, text="Quantity",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=560,y=230)
quantity_entry = Spinbox(tk, from_=0,to=100,font=("Arial", 12),bd=3)
quantity_entry.place(x=500,y=260)

price_label = Label(tk, text="Unit Price",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=870,y=230)
price_entry = Spinbox(tk,from_=0.0, to=5000, increment=0.5,font=("Arial", 12),bd=3)
price_entry.place(x=810,y=260)

add_item_button = Button(tk, text="Add item",font=("Arial", 10,"bold"),bg="#1A374D",fg="#F5F5F5",command=add_item)
add_item_button.place(x=1110,y=255)

columns = ('particulars', 'quantity', 'unit_price', 'amount')
tree = ttk.Treeview(tk, columns=columns, show="headings")
tree.heading('particulars', text='Particulars')
tree.heading('quantity', text='Quantity')
tree.heading('unit_price', text='Unit Price')
tree.heading('amount', text="Amount")
tree.place(x=190,y=350)

edit_btn = ttk.Button(tk,text="Edit", command=edit_selection)
edit_btn.place(x=915,y=580)

stotal_label = Label(tk, text="Sub Total : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=350)
stotal_entry = Entry(tk,font=("Arial", 12),bd=3)
stotal_entry.place(x=1210,y=350)
stotal_entry.insert(0,"0.0")

cgst_label = Label(tk, text="CGST @9% : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=400)
cgst_entry = Entry(tk,font=("Arial", 12),bd=3)
cgst_entry.place(x=1210,y=400)
cgst_entry.insert(0,"0.0")

sgst_label = Label(tk, text="SGST @9% : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=450)
sgst_entry = Entry(tk,font=("Arial", 12),bd=3)
sgst_entry.place(x=1210,y=450)
sgst_entry.insert(0,"0.0")

gtotal_label = Label(tk, text="Grand Total : ",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=1100,y=500)
gtotal_entry = Entry(tk,font=("Arial", 12, "bold"),bd=3)
gtotal_entry.place(x=1210,y=500)
gtotal_entry.insert(0,"0.0")

save_invoice_button = Button(tk, text="Generate Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2)
save_invoice_button.place(x=650,y=640)

new_invoice_button = Button(tk, text="New Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2)
new_invoice_button.place(x=650,y=700)

view_invoice_button = Button(tk, text="View Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2)
view_invoice_button.place(x=650,y=760)

tk.mainloop()

from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import time
from tkinter import messagebox

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Invoice - Ajra Tex")
tk.configure(bg='white')

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
    
def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_number_entry.get()
    gst = gst_entry.get()
    current_date = datetime.date.today()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    subtotal = sum(item[3] for item in invoice_list)
    cgst = subtotal*0.09
    sgst = subtotal*0.09
    gtotal = subtotal+cgst+sgst
        
    doc.render({"name":name,
                "address":address,
                "phone":phone,
                "gst":gst,
                "invoicedate":current_date,
                "invoicetime":current_time,
                "invoice_list": invoice_list,
                "subtotal":subtotal,
                "cgst":cgst,
                "sgst":sgst,
                "gtotal":gtotal})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")

Label(tk,text="\n",bg="white",fg="#1A374D").pack()
a = Label(tk,text="AJRA TEX - KARUR",font=("Arial", 30, "bold"),bg="white",fg="#1A374D").pack()

'''------- Buyer details -------'''

name_label = Label(tk, text="Name",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=260,y=100)
name_entry = Entry(tk,font=("Arial", 12),bd=3)
name_entry.place(x=190,y=130)

address_label = Label(tk, text="Address",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=560,y=100)
address_entry = Entry(tk,font=("Arial", 12),bd=3)
address_entry.place(x=500,y=130)

phone_number_label = Label(tk, text="Phone number",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=850,y=100)
phone_number_entry = Entry(tk,font=("Arial", 12),bd=3)
phone_number_entry.place(x=810,y=130)

gst_label = Label(tk, text="GST number",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=1160,y=100)
gst_entry = Entry(tk,font=("Arial", 12),bd=3)
gst_entry.place(x=1110,y=130)

'''------- Product details -------'''

particulars_label = Label(tk, text="Particulars",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=240,y=180)
particulars_entry = Entry(tk,font=("Arial", 12),bd=3)
particulars_entry.place(x=190,y=210)

quantity_label = Label(tk, text="Quantity",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=560,y=180)
quantity_entry = Spinbox(tk, from_=1,to=100,font=("Arial", 12),bd=3)
quantity_entry.place(x=500,y=210)

price_label = Label(tk, text="Unit Price",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=870,y=180)
price_entry = Spinbox(tk,from_=0.0, to=5000, increment=0.5,font=("Arial", 12),bd=3)
price_entry.place(x=810,y=210)

add_item_button = Button(tk, text="Add item",font=("Arial", 10,"bold"),bg="#1A374D",fg="#F5F5F5",command=add_item)
add_item_button.place(x=1110,y=210)

columns = ('particulars', 'quantity', 'unit_price', 'amount')
tree = ttk.Treeview(tk, columns=columns, show="headings")
tree.heading('particulars', text='Particulars')
tree.heading('quantity', text='Quantity')
tree.heading('unit_price', text='Unit Price')
tree.heading('amount', text="Amount")
tree.place(x=190,y=300)

stotal_label = Label(tk, text="Sub Total : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=300)
stotal_entry = Entry(tk,font=("Arial", 12),bd=3)
stotal_entry.place(x=1210,y=300)

cgst_label = Label(tk, text="CGST @9% : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=350)
cgst_entry = Entry(tk,font=("Arial", 12),bd=3)
cgst_entry.place(x=1210,y=350)

sgst_label = Label(tk, text="SGST @9% : ",font=("Arial", 12),bg="white",fg="#1A374D").place(x=1100,y=400)
sgst_entry = Entry(tk,font=("Arial", 12),bd=3)
sgst_entry.place(x=1210,y=400)

gtotal_label = Label(tk, text="Grand Total : ",font=("Arial", 12,"bold"),bg="white",fg="#1A374D").place(x=1100,y=500)
gtotal_entry = Entry(tk,font=("Arial", 12, "bold"),bd=3)
gtotal_entry.place(x=1210,y=500)

save_invoice_button = Button(tk, text="Generate Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2,command=generate_invoice)
save_invoice_button.place(x=650,y=580)
new_invoice_button = Button(tk, text="New Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2)
new_invoice_button.place(x=650,y=640)
edit_invoice_button = Button(tk, text="Edit Invoice",font=("Arial",10,"bold"),bg="#1A374D",fg="#F5F5F5",width=30,height=2)
edit_invoice_button.place(x=650,y=700)

tk.mainloop()

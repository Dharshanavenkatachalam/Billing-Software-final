from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
from datetime import date
import time
from tkinter import messagebox
import mysql.connector as sql

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Report and Analysis - Ajra Tex")
tk.configure(bg='white')

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="ajra")
cursor=mycon.cursor()

def display_block():
    Label(tk,text="Product History",font=("Arial", 15, "bold"),bg="white",fg="#1A374D").place(x=180,y=100)
    show = ("SELECT particulars, quantity FROM invoice")
    cursor.execute(show)
    data=cursor.fetchall()
    
    product = []
    price = []
    dproduct = []
    dprice = []
    
    for i in range(0,len(data)):
        for j in (data[i][0].split(",")):
            product.append(j)
        for j in (data[i][1].split(",")):
            price.append(j)
    
    for i in range(len(product)):
        if(product[i] in dproduct):
            dprice[dproduct.index(product[i])] += int(price[i])
        else:
            dproduct.append(product[i])
            dprice.append(int(price[i]))
    
    columns = ('particulars', 'quantity')
    tree = ttk.Treeview(tk, columns=columns, show="headings")
    tree.heading('particulars', text='Particulars')
    tree.heading('quantity', text='Quantity')
    tree.place(x=50,y=150)           
    
    for i in range(len(dprice)):
        row = [dproduct[i],dprice[i]]
        tree.insert('',0, values=row)
    
Label(tk,text="AJRA TEX - KARUR",font=("Arial", 20, "bold"),bg="white",fg="#1A374D").place(x=650,y=20)
display_block()

tk.mainloop()
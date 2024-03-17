from tkinter import *

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Home Page - Ajra Tex")
tk.configure(bg='white')

def invoice():
    tk.destroy()
    import invoice
    
Label(tk,text="\n",bg="white",fg="#1A374D").pack()
a = Label(tk,text="AJRA TEX - KARUR",font=("Ailerons",40),bg="white",fg="#1A374D").pack()
bt1 = Button(tk,text="Invoice",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",height=3,width=15, command=invoice).place(x=400,y=250)
bt2 = Button(tk,text="Delivery Slip",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",height=3,width=15).place(x=900,y=250)
bt3 = Button(tk,text="Expense Tracker",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",height=3,width=15).place(x=400,y=500)
bt4 = Button(tk,text="Report & Analysis",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",height=3,width=15).place(x=900,y=500)

tk.mainloop()

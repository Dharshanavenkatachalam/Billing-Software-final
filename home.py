from tkinter import *


tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Ajra Tex - Karur")
tk.configure(bg='white')

def login():
    en1 = c1.get()
    en2 = d1.get()
    
    if(en1 == "ajratex" and en2 == "password"):
        tk.destroy()
        import mainpage
        
Label(tk,text="\n",bg="white",fg="#1A374D").pack()
a = Label(tk,text="AJRA TEX - KARUR",font=("Ailerons",40),bg="white",fg="#1A374D").pack()
b = Label(tk,text="\nLOGIN",font=("Archivo SemiCondensed Black",30),bg="white",fg="#1A374D").pack()
c = Label(tk,text="\nUSERNAME",font=("Archivo Expanded",20),bg="white",fg="#1A374D").pack()
c1 = Entry(tk,font=("Calibri",18),bd=5,justify="center")
c1.pack()
d = Label(tk,text="\nPASSWORD",font=("Archivo Expanded",20),bg="white",fg="#1A374D").pack()
d1 = Entry(tk,font=("Calibri",18),show="*",bd=5,justify="center")
d1.pack()
Label(tk,text="\n",bg="white").pack()
bt1 = Button(tk,text="LOGIN",font=("Archivo Expanded",15),bg="#1A374D",fg="#F5F5F5",command = login).pack()

tk.mainloop()

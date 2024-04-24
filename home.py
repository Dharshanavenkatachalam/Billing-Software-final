from tkinter import *

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Ajra Tex - Karur")
tk.configure(bg='white')

def login():
    en1 = c1.get()
    en2 = d1.get()
    
    if(en1 == "" and en2 == ""):
        tk.destroy()
        import mainpage
        
Label(tk,text="\n",bg="white",fg="#1A374D").pack()
a = Label(tk,text="AJRA TEX - KARUR",font=("Arial",30, "bold"),bg="white",fg="#1A374D").pack()
b = Label(tk,text="LOGIN",font=("Arial",20,"bold"),bg="white",fg="#1A374D").place(x=720,y=130)
c = Label(tk,text="USERNAME",font=("Arial",20),bg="white",fg="#1A374D").place(x=700,y=250)
c1 = Entry(tk,font=("Calibri",18),bd=5,justify="center")
c1.place(x=650,y=300)
d = Label(tk,text="PASSWORD",font=("Arial",20),bg="white",fg="#1A374D").place(x=700,y=400)
d1 = Entry(tk,font=("Calibri",18),show="*",bd=5,justify="center")
d1.place(x=650,y=450)
bt1 = Button(tk,text="LOGIN",font=("Arial",15),bg="#1A374D",fg="#F5F5F5",width=10,height=1,command = login).place(x=720,y=550)

tk.mainloop()

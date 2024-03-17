from tkinter import *
from tkinter import ttk

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Invoice - Ajra Tex")
tk.configure(bg='white')

t1=0
t2=0
t3=0
t4=0
t5=0
t6=0
t7=0
t8=0
t9=0
t10=0

def submit():
    ea1 = int(d1.get())
    ea2 = d2.get()
    ea3 = d3.get()
    ea4 = d4.get()
    ea5 = d5.get()
    ea6 = d6.get()
    ea7 = d7.get()
    ea8 = d8.get()
    ea9 = d9.get()
    ea10 = d10.get()
    
    eb1 = int(e1.get())
    eb2 = e2.get()
    eb3 = e3.get()
    eb4 = e4.get()
    eb5 = e5.get()
    eb6 = e6.get()
    eb7 = e7.get()
    eb8 = e8.get()
    eb9 = e9.get()
    eb10 = e10.get()
    
    t1=ea1*eb1
    # t2=ea2*eb2
    # t3=ea3*eb3
    # t4=ea4*eb4
    # t5=ea5*eb5
    # t6=ea6*eb6
    # t7=ea7*eb7
    # t8=ea8*eb8
    # t9=ea9*eb9
    # t10=ea10*eb10
    
Label(tk,text="\n",bg="white",fg="#1A374D").pack()
a = Label(tk,text="AJRA TEX - KARUR",font=("Ailerons",40),bg="white",fg="#1A374D").pack()

b = Label(tk,text="Particulars",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=400,y=150)
c = Label(tk,text="Size",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=640,y=150)
d = Label(tk,text="Quantity",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=745,y=150)
e = Label(tk,text="Rate",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=900,y=150)
f = Label(tk,text="Amount",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=150)
g = Label(tk,text="Invoice Number: ",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=50)

line = Label(tk,text="------------------------",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1300,y=150)
total = Label(tk,text="Total : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=190)
cgst = Label(tk,text="CGST : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=230)
sgst = Label(tk,text="SGST : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=270)
gt = Label(tk,text="Grand Total: 10000000",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=340)
line = Label(tk,text="------------------------",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1300,y=370)

btn1 = Button(tk,text="Submit",font=("Archivo Expanded",13),fg="white",bg="#1A374D",command=submit).place(x=1350,y=500)
btn2 = Button(tk,text="Print Invoice",font=("Archivo Expanded",13),fg="white",bg="#1A374D").place(x=1330,y=560)
btn3 = Button(tk,text="Download Invoice",font=("Archivo Expanded",13),fg="white",bg="#1A374D").place(x=1300,y=620)

b1=Entry(tk,font=("Archivo Expanded",13),bd=2)
b2=Entry(tk,font=("Archivo Expanded",13),bd=2)
b3=Entry(tk,font=("Archivo Expanded",13),bd=2)
b4=Entry(tk,font=("Archivo Expanded",13),bd=2)
b5=Entry(tk,font=("Archivo Expanded",13),bd=2)
b6=Entry(tk,font=("Archivo Expanded",13),bd=2)
b7=Entry(tk,font=("Archivo Expanded",13),bd=2)
b8=Entry(tk,font=("Archivo Expanded",13),bd=2)
b9=Entry(tk,font=("Archivo Expanded",13),bd=2)
b10=Entry(tk,font=("Archivo Expanded",13),bd=2)

c1=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c2=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c3=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c4=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c5=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c6=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c7=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c8=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c9=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
c10=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")

d1=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d2=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d3=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d4=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d5=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d6=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d7=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d8=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d9=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d10=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")

e1=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e2=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e3=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e4=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e5=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e6=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e7=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e8=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e9=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e10=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")

f1 = Label(tk,text=str(t1),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=200)
f2 = Label(tk,text=str(t2),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=260)
f3 = Label(tk,text=str(t3),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=320)
f4 = Label(tk,text=str(t4),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=380)
f5 = Label(tk,text=str(t5),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=440)
f6 = Label(tk,text=str(t6),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=500)
f7 = Label(tk,text=str(t7),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=560)
f8 = Label(tk,text=str(t8),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=620)
f9 = Label(tk,text=str(t9),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=680)
f10 = Label(tk,text=str(t10),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1100,y=740)

b1.place(x=320,y=200)
b2.place(x=320,y=260)
b3.place(x=320,y=320)
b4.place(x=320,y=380)
b5.place(x=320,y=440)
b6.place(x=320,y=500)
b7.place(x=320,y=560)
b8.place(x=320,y=620)
b9.place(x=320,y=680)
b10.place(x=320,y=740)

c1.place(x=630,y=200)
c2.place(x=630,y=260)
c3.place(x=630,y=320)
c4.place(x=630,y=380)
c5.place(x=630,y=440)
c6.place(x=630,y=500)
c7.place(x=630,y=560)
c8.place(x=630,y=620)
c9.place(x=630,y=680)
c10.place(x=630,y=740)

d1.place(x=760,y=200)
d2.place(x=760,y=260)
d3.place(x=760,y=320)
d4.place(x=760,y=380)
d5.place(x=760,y=440)
d6.place(x=760,y=500)
d7.place(x=760,y=560)
d8.place(x=760,y=620)
d9.place(x=760,y=680)
d10.place(x=760,y=740)

e1.place(x=880,y=200)
e2.place(x=880,y=260)
e3.place(x=880,y=320)
e4.place(x=880,y=380)
e5.place(x=880,y=440)
e6.place(x=880,y=500)
e7.place(x=880,y=560)
e8.place(x=880,y=620)
e9.place(x=880,y=680)
e10.place(x=880,y=740)

tk.mainloop()
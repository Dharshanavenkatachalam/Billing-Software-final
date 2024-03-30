from tkinter import *
from tkinter import ttk

tk=Tk()
tk.geometry("1920x1080")
tk.config(bg="#F5F5F5")
tk.title("Invoice - Ajra Tex")
tk.configure(bg='white')

def submit():
    t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 = 0
    ea1 = float(d1.get())
    ea2 = float(d2.get())
    ea3 = float(d3.get())
    ea4 = float(d4.get())
    ea5 = float(d5.get())
    ea6 = float(d6.get())
    ea7 = float(d7.get())
    ea8 = float(d8.get())
    ea9 = float(d9.get())
    ea10 = float(d10.get())
    
    eb1 = float(e1.get())
    eb2 = float(e2.get())
    eb3 = float(e3.get())
    eb4 = float(e4.get())
    eb5 = float(e5.get())
    eb6 = float(e6.get())
    eb7 = float(e7.get())
    eb8 = float(e8.get())
    eb9 = float(e9.get())
    eb10 = float(e10.get())
    
    t1=ea1*eb1
    t2=ea2*eb2
    t3=ea3*eb3
    t4=ea4*eb4
    t5=ea5*eb5
    t6=ea6*eb6
    t7=ea7*eb7
    t8=ea8*eb8
    t9=ea9*eb9
    t10=ea10*eb10
    
    tot = t1+t2+t3+t4+t5+t6+t7+t8+t9+t10
    cg = tot*0.09
    sg = tot*0.09
    gtotal = tot+cg+sg
    Label(tk,text=tot,font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1370,y=190)
    Label(tk,text=cg,font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1370,y=230)
    Label(tk,text=sg,font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1370,y=270)
    Label(tk,text=gtotal,font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1420,y=340)
    
    f1 = Label(tk,text=str(t1),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=200)
    f2 = Label(tk,text=str(t2),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=260)
    f3 = Label(tk,text=str(t3),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=320)
    f4 = Label(tk,text=str(t4),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=380)
    f5 = Label(tk,text=str(t5),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=440)
    f6 = Label(tk,text=str(t6),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=500)
    f7 = Label(tk,text=str(t7),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=560)
    f8 = Label(tk,text=str(t8),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=620)
    f9 = Label(tk,text=str(t9),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=680)
    f10 = Label(tk,text=str(t10),font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=980,y=740)
    

a = Label(tk,text="AJRA TEX - KARUR",font=("Ailerons",40),bg="white",fg="#1A374D").pack()
inv = Label(tk,text="Invoice Number: ",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=520,y=90)
invi=Entry(tk,font=("Archivo Expanded",13),width=15,bd=2,justify="center")
invbtn = Button(tk,text="Search",font=("Archivo Expanded",10),bg="#1A374D",fg="white").place(x=950,y=92)

b = Label(tk,text="Particulars",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=175,y=150)
c = Label(tk,text="Size",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=460,y=150)
d = Label(tk,text="Quantity",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=585,y=150)
e = Label(tk,text="Rate",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=775,y=150)
f = Label(tk,text="Amount",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=950,y=150)

line = Label(tk,text="------------------------",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1300,y=150)
total = Label(tk,text="Total : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=190)
cgst = Label(tk,text="CGST : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=230)
sgst = Label(tk,text="SGST : ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=270)
gt = Label(tk,text="Grand Total: ",font=("Archivo Expanded",12),bg="white",fg="#1A374D").place(x=1300,y=340)
line = Label(tk,text="------------------------",font=("Archivo Expanded",15),bg="white",fg="#1A374D").place(x=1300,y=370)

btn1 = Button(tk,text="Submit",font=("Archivo Expanded",13),fg="white",bg="#1A374D",command=submit).place(x=1350,y=500)
btn2 = Button(tk,text="Print Invoice",font=("Archivo Expanded",13),fg="white",bg="#1A374D").place(x=1330,y=560)
btn3 = Button(tk,text="Download Invoice",font=("Archivo Expanded",13),fg="white",bg="#1A374D").place(x=1300,y=620)

#Particulars
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

#Size
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

#Quantity
d1=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d1.insert(END,"0")
d2=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d2.insert(0,"0")
d3=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d3.insert(0,"0")
d4=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d4.insert(0,"0")
d5=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d5.insert(0,"0")
d6=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d6.insert(0,"0")
d7=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d7.insert(0,"0")
d8=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d8.insert(0,"0")
d9=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d9.insert(0,"0")
d10=Entry(tk,font=("Archivo Expanded",13),width=5,bd=2,justify="center")
d10.insert(0,"0")

#Rate
e1=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e1.insert(0,"0")
e2=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e2.insert(0,"0")
e3=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e3.insert(0,"0")
e4=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e4.insert(0,"0")
e5=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e5.insert(0,"0")
e6=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e6.insert(0,"0")
e7=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e7.insert(0,"0")
e8=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e8.insert(0,"0")
e9=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e9.insert(0,"0")
e10=Entry(tk,font=("Archivo Expanded",13),width=8,bd=2,justify="center")
e10.insert(0,"0")

invi.place(x=720,y=93)

b1.place(x=100,y=200)
b2.place(x=100,y=260)
b3.place(x=100,y=320)
b4.place(x=100,y=380)
b5.place(x=100,y=440)
b6.place(x=100,y=500)
b7.place(x=100,y=560)
b8.place(x=100,y=620)
b9.place(x=100,y=680)
b10.place(x=100,y=740)

c1.place(x=450,y=200)
c2.place(x=450,y=260)
c3.place(x=450,y=320)
c4.place(x=450,y=380)
c5.place(x=450,y=440)
c6.place(x=450,y=500)
c7.place(x=450,y=560)
c8.place(x=450,y=620)
c9.place(x=450,y=680)
c10.place(x=450,y=740)

d1.place(x=600,y=200)
d2.place(x=600,y=260)
d3.place(x=600,y=320)
d4.place(x=600,y=380)
d5.place(x=600,y=440)
d6.place(x=600,y=500)
d7.place(x=600,y=560)
d8.place(x=600,y=620)
d9.place(x=600,y=680)
d10.place(x=600,y=740)

e1.place(x=750,y=200)
e2.place(x=750,y=260)
e3.place(x=750,y=320)
e4.place(x=750,y=380)
e5.place(x=750,y=440)
e6.place(x=750,y=500)
e7.place(x=750,y=560)
e8.place(x=750,y=620)
e9.place(x=750,y=680)
e10.place(x=750,y=740)

tk.mainloop()
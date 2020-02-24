from tkinter import *
import calendar

root = Tk()
root.title("Calendar/Calendário")
root.geometry("260x230")
root.resizable(0,0)

def show():
    month = int(spin1.get())
    year = int(spin2.get())
    cal = calendar.month(year,month)

    txt.delete(0.0,END)
    txt.insert(INSERT, cal)
lbl1 = Label(root,text="Month/Mês", font=('arial',9,'bold')).place(x=15,y=0)
lbl2 = Label(root,text="Year/Ano", font=('arial',9,'bold')).place(x=120,y=0)


spin1 = Spinbox(root,from_=1,to=12,width=4)
spin1.place(x=80,y=0)
spin2 = Spinbox(root,from_=1999,to=2100,width=4)
spin2.place(x=180,y=0)

btn = Button(root, text="show",font=('arial',9,'bold'),command=show).place(x=100,y=30)

txt = Text(root, width=24,height=8)
txt.place(x=20,y=47)

root.mainloop()

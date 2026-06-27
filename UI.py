from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
main=tk.Tk()
main.geometry('1200x800')#size of the window 
main.title('SSJ')#title of the window
main.config(bg="orange")#colour of the screen in window


#label
l=Label(main,font=("Roboto",20),fg='black',text="Create Account").place(x=500,y=200)
nl=Label(main,font=("Arial",17),fg='blue',text="Name").place(x=500,y=300)
pl=Label(main,font=("Arial",17),fg='blue',text="Pass Word").place(x=500,y=350)


def show():
    
    name=ne.get()
    pwd=pe.get()
    print("NAME:",name)
    print("PASSWORD",pwd)

    
ne=Entry(main)
ne.place(x=600,y=300)#.grid(row=0,coloumn=2)
pe=Entry(main)
pe.place(x=650,y=350)#.grid(row=2,coloumn=1)

Button(main,text='sumbit',command=show).place(x=800,y=600)


places=Combobox(main)
places=[values]=("select","TN","UP","AP","MP")
place.current(0)
places.place(x=700,y=650)


rb=Radiobutton(main,text="male",value=0)
rb.place(x=800,y=650)
rb1=Radiobutton(main,text="female",value=1)
rb1.place(x=900,y=650)


gender=StringVar(value="Male")

rb=Radiobutton(main,text="Male",variable=gender,value="Male")
rb.place(x=300,y=400)
rb1=Radiobutton(main,text="Female",variable=gender,value="Female")
rb1.place(x=400,y=400)

































































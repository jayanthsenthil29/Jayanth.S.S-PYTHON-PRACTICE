from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
page = tk.Tk()
page.geometry("800x600")
page.title("page")
page.config(bg = "light yellow")

l = Label(page,font =("Helvetica (Bold)",23),fg = "black",bg = "white",text = "WELCOME TO OUR WEBSITE").place(x=200,y=100)

n = Label(page,font = ("Roboto(Bold)",21),fg = "black",bg = "white",text = "NAME :").place(x = 280,y =280)

p = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "PASSWORD :").place(x = 280,y = 330)

a = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "AGE :").place(x = 280,y = 380)

c = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "CONTACT NUMBER :").place(x = 280,y = 440)

b = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "STATE :").place(x = 280,y = 500)

g = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "EMAIL :").place(x = 280,y = 560)

t = Label(page,font = ("Roboto",19),fg = "black",bg = "white",text = "GENDER :").place(x = 280,y = 620)

def show():
    NAME = ne.get()
    PASSWORD= pe.get()
    AGE= ae.get()
    CONTACT_NUMBER = ce.get()
    STATE = be.get()
    EMAIL = ge.get()
    GENDER= te.get()

    print("NAME :",NAME)
    print("PASSWORD :",PASSWORD)
    print("AGE :",AGE)
    print("CONTACT_NUMBER :",CONTACT_NUMBER)
    print("STATE :",STATE)
    print("EMAIL :",EMAIL)
    print("GENDER :",GENDER)

ne= Entry(page)
ne.place(x=430,y=290)
pe= Entry(page)
pe.place(x=450,y=340)
ae=Entry(page)
ae.place(x=400,y=390)
ce=Entry(page)
ce.place(x=550,y=450)
be=Entry(page)
be.place(x=460,y=510)
ge=Entry(page)
ge.place(x=400,y=570)
te=Entry(page)
te.place(x=460,y=630)


Button(page,text = 'Register',command = show).place(x =280,y = 700)



places = Combobox(page)
places["values"] = ("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal")
places.current(0)
places.place(x = 460,y = 510)


page.mainloop()





















    






    



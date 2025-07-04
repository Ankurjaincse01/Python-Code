from tkinter import *

# Creating Main Window
r = Tk()
r.geometry("400x400")
r.title("My Title")
r.configure(bg="Orange")



# Adding Labels in Main Window
rn = Label(r,text="Roll No")
rn.place(x=20,y=20)

fn = Label(r,text="Firstname")
fn.place(x=20,y=60)

ln = Label(r,text="Lastname")
ln.place(x=20,y=100)

em = Label(r,text="Email")
em.place(x=20,y=140)


ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=60)

eln = Entry()
eln.place(x=100,y=100)

eem = Entry()
eem.place(x=100,y=140)


# Adding Buttons into Main Window
button1 = Button(r,text="Button1",bg="White")
button1.place(x=20,y=200)
mainloop()
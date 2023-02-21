from tkinter import *

root=Tk()
def Login():
    Z=Tk()
    user=c.get()
    pas=e.get()
    if x==user and y==pas:
        f=Label (Z, text="Welcome").pack()
    elif x==user and y!=pas:
        f=Label (Z,text="Invalid password").pack()
    else:
        f=Label (Z,text="Access denied").pack()
        
    
    

    Z.mainloop()
x = "Olaide"
y = "9919"
a=Label (root, text="LOGIN FORM", bg="white", fg="black").pack()
b=Label (root, text="Username", bg="white", fg="black").pack()
c=Entry (root)
c.pack()
d=Label (root, text="Password", bg="white", fg="black").pack()
e=Entry (root)
e.pack()    
f=Button (root, text="Login", command=Login).pack()
#f.bind("<Button>", )

root.mainloop
 

from tkinter import*

root=Tk()

a=Label (root, text="BIODATA FORM", bg="white", fg="black").grid(row=1, column=2)
b=Label (root, text="Surname", bg="white", fg="black").grid(row=2, column=1)
c=Entry (root, text="Surname").grid(row=2, column=2)
d=Label (root, text="First Name", bg="white", fg="black").grid(row=3, column=1)
e=Entry (root, text="First Name").grid(row=3, column=2)
f=Label (root, text="Second Name", bg="white", fg="black").grid(row=4, column=1)
g=Entry (root, text="Second Name").grid(row=4, column=2)
h=Label (root, text="Gender", bg="white", fg="black").grid(row=5, column=1)
i=Entry (root, text="Gender").grid(row=5, column=2)
j=Label (root, text="Nationality", bg="white", fg="black").grid(row=6, column=1)
k=Entry (root, text="Nationality").grid(row=6, column=2)
l=Label (root, text="State of origin", bg="white", fg="black").grid(row=7, column=1)
m=Entry (root, text="State of origin").grid(row=7, column=2)
n=Label (root, text="Local Government of origin", bg="white", fg="black").grid(row=8, column=1)
o=Entry (root, text="Local Government of origin").grid(row=8, column=2)
p=Button (root, text="Submit", bg="white", fg="black").grid(row=9, column=2)


root.mainloop()

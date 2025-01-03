from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
window=Tk()
co0="#ffffff"
window.geometry("800x500")
global sno
sno=1
window.title("Contact book")
window.configure(background=co0)
myfont=Font(family="Algerian",weight="bold", underline=True)
lab=Label(window,text="CONTACTBOOK", font=(myfont,15), background="white")
lab.pack(side=TOP)
def addRecord():
    global sno
    myTree.insert("",index="end",iid=sno,values=(sno,txtname.get(),txtadd.get(),txtcon.get(),txtemail.get()))
    txtname.delete(0,END)
    txtadd.delete(0,END)
    txtcon.delete(0,END)
    txtemail.delete(0,END)
    sno+=1

def selectRecord():
    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtemail.delete(0, END)
    selected=myTree.focus()
    values=myTree.item(selected,'values')
    #messagebox.showinfo("Message",values)
    txtname.insert(0,values[1])
    txtadd.insert(0, values[2])
    txtcon.insert(0, values[3])
    txtemail.insert(0, values[4])

def updateRecord():
    no=myTree.focus()[0]#column id
    selected=myTree.focus()#row id
    myTree.item(selected,values=(no, txtname.get(), txtadd.get(), txtcon.get(), txtemail.get()))
    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtemail.delete(0, END)


def deleteRecord():
    record=myTree.selection()[0]
    myTree.delete(record)
    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtemail.delete(0, END)

def viewRecord():
    txtname.delete(0, END)
    txtadd.delete(0, END)
    txtcon.delete(0, END)
    txtemail.delete(0, END)
    selected = myTree.focus()
    values = myTree.item(selected, 'values')
    # messagebox.showinfo("Message",values)
    txtname.insert(0, values[1])
    txtadd.insert(0, values[2])
    txtcon.insert(0, values[3])
    txtemail.insert(0, values[4])

#Frame 1
myFrame=Frame(window)
myFrame.pack()
lblname=Label(myFrame,text="Name",font=("times",15,"bold"),pady=5)
lblname.grid(row=1, column=0,sticky=NE)
txtname=Entry(myFrame,font=("time",15))
txtname.grid(row=1, column=1)

lbladd=Label(myFrame,text="Address",font=("times",15,"bold"),pady=5)
lbladd.grid(row=2, column=0,sticky=NE)
txtadd=Entry(myFrame,font=("time",15))
txtadd.grid(row=2, column=1)

lblcon=Label(myFrame,text="Contact",font=("times",15,"bold"),pady=5)
lblcon.grid(row=3, column=0,sticky=NE)
txtcon=Entry(myFrame,font=("time",15))
txtcon.grid(row=3, column=1)

lblemail=Label(myFrame,text="Email",font=("times",15,"bold"),pady=5)
lblemail.grid(row=4, column=0,sticky=NE)
txtemail=Entry(myFrame,font=("time",15))
txtemail.grid(row=4, column=1)

#Frame 2
btnFrame=Frame(window)
btnFrame.pack()

btnAdd=Button(btnFrame,text="Add", bg="#1289A7", width=5, padx=5, pady=5, font=("times",14,"bold"),command=addRecord)
btnAdd.grid(row=1, column=0, pady=10, padx=5)

btnSelect=Button(btnFrame,text="Select", bg="#10Ac84", width=5, padx=5, pady=5, font=("times",14,"bold"),command=selectRecord)
btnSelect.grid(row=1, column=1, pady=10, padx=5)

btnUpdate=Button(btnFrame,text="Update", bg="#3c6382", width=5, padx=5, pady=5, font=("times",14,"bold"),command=updateRecord)
btnUpdate.grid(row=1, column=2, pady=10, padx=5)

btnDelete=Button(btnFrame,text="Delete", bg="#d63031", width=5, padx=5, pady=5, font=("times",14,"bold"),command=deleteRecord)
btnDelete.grid(row=1, column=3, pady=10, padx=5)

btnView=Button(btnFrame,text="View", bg="#01a3a4", width=5, padx=5, pady=5, font=("times",14,"bold"),command=viewRecord)
btnView.grid(row=1, column=4, pady=10, padx=5)

#Treeview

myTree=ttk.Treeview(window)
myTree['column']=('S.no','Name','Address','Contact','Email')
myTree.column('#0', width=0,stretch=NO)
myTree.column('#1',width=30)
myTree.column('#2',width=80)
myTree.column('#3',width=80)
myTree.column('#4',width=80)
myTree.column('#5',width=80)

myTree.heading("#0",text="")
myTree.heading("#1",text="S.NO")
myTree.heading("#2",text="NAME")
myTree.heading("#3",text="ADDRESS")
myTree.heading("#4",text="CONTACT")
myTree.heading("#5",text="EMAIL")

data=[
    ["Sathya","Salem","9066592043","sathya@gmail.com"],
    ["Santhi","Chennai","9781592043","santhi@gmail.com"],
    ["Rameya","Trichy","8436092043","rameya@gmail.com"],
    ["Arun","Pondicherry","9901710106","arun@gmail.com"],
    ["Shakthi","Karaikal","9486115357","shakthi@gmail.com"],
    ["Mani","Chennai","9066525694","mani@gmail.com"]
]
for datas in data:
    myTree.insert("",index="end",iid=sno,values=(sno,datas[0],datas[1],datas[2],datas[3]))
    sno+=1

myTree.pack(fill=X)

mainloop()
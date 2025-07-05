import tkinter as t
from tkinter import font
from tkinter import messagebox
import mysql.connector


root=t.Tk()
root.title("Voting System")
root.geometry("800x800")
root.configure(bg="sky blue")


def submit():
    
    useraadhar = taadhar.get()
    username = tname.get()
    father = tfather.get()
    userage = tage.get()
    usercity = tcity.get()
    password = tpass.get()
    pincode = tpin.get()
    address = taddress.get()
    mobile = tmob.get()
    print(useraadhar)
    print(username)
    print(father)
    print(userage)
    print(usercity)
    print(password)
    print(pincode)
    print(address)
    print(mobile)
    
    db=mysql.connector.connect(host='localhost',user='root',database='VotingSystem',password='')
    cur=db.cursor()
    cur.execute("create table if not exists myuser(aadhar double primary key, name Text, fathername text,age integer,city text,password text,pincode integer,address text ,mobileno double)")
    print("Table Created")
    #Check if any field is empty
    if not all([useraadhar, username, father, userage, usercity, password, pincode, address, mobile]):
        messagebox.showwarning("Incomplete Details", "Please fill all the fields.")
        return
    try:

        q="insert into myuser values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        v=(useraadhar,username,father,userage,usercity,password,pincode,address,mobile)
        cur.execute(q,v)
        db.commit()
        print("Data Inserted")
        messagebox.showinfo("Success", "Registration Successful!")
        root.destroy()
    except Exception as e:
        print("Error inserting data:", e)
    


lhead =t.Label(root,text='User Registration',font=('monotype corsiva',18),width="50",fg="black",bg="white")
lhead.grid(row=0,column=1,padx=10,pady=10) 

laadhar =t.Label(root,text='Aadhar No',font=('bell mt',18),fg="black",bg="white")     
laadhar.grid(row=1,column=0,padx=10,pady=10)

lname =t.Label(root,text='Name',font=('bell mt',18),fg="black",bg="white")     
lname.grid(row=2,column=0,padx=10,pady=10)

lfather =t.Label(root,text='Father name',font=('bell mt',18),fg="black",bg="white")     
lfather.grid(row=3,column=0,padx=10,pady=10)

lage=t.Label(root,text='Age',font=('bell mt',18),fg="black",bg="white")     
lage.grid(row=4,column=0,padx=10,pady=10)

lcity =t.Label(root,text='City',font=('bell mt',18),fg="black",bg="white")     
lcity.grid(row=5,column=0,padx=10,pady=10)

lpass =t.Label(root,text='Password',font=('bell mt',18),fg="black",bg="white")     
lpass.grid(row=6,column=0,padx=10,pady=10)

lpin =t.Label(root,text='Pinocde',font=('bell mt',18),fg="black",bg="white")     
lpin.grid(row=7,column=0,padx=10,pady=10)

laddress =t.Label(root,text='Address',font=('bell mt',18),fg="black",bg="white")     
laddress.grid(row=8,column=0,padx=10,pady=10)

lmob =t.Label(root,text='Mobile No',font=('bell mt',18),fg="black",bg="white")     
lmob.grid(row=9,column=0,padx=10,pady=10)


taadhar =t.Entry(root,font=('bell mt',18),width="50")               
taadhar.grid(row=1,column=1,padx=10,pady=10)

tname =t.Entry(root,font=('bell mt',18),width="50")               
tname.grid(row=2,column=1,padx=10,pady=10)

tfather =t.Entry(root,font=('bell mt',18),width="50")               
tfather.grid(row=3,column=1,padx=10,pady=10)

tage =t.Entry(root,font=('bell mt',18),width="50")               
tage.grid(row=4,column=1,padx=10,pady=10)

tcity =t.Entry(root,font=('bell mt',18),width="50")               
tcity.grid(row=5,column=1,padx=10,pady=10)

tpass =t.Entry(root,font=('bell mt',18),width="50",show="*")               
tpass.grid(row=6,column=1,padx=10,pady=10)

tpin =t.Entry(root,font=('bell mt',18),width="50")               
tpin.grid(row=7,column=1,padx=10,pady=10)

taddress =t.Entry(root,font=('bell mt',18),width="50")               
taddress.grid(row=8,column=1,padx=10,pady=10)

tmob =t.Entry(root,font=('bell mt',18),width="50")               
tmob.grid(row=9,column=1,padx=10,pady=10)

submit=t.Button(root,text="SUBMIT",font=('bell mt',20,'bold'),bg='green',fg='black',command=submit)
submit.grid(row=10,column=1,padx=10,pady=10)

root.mainloop()    
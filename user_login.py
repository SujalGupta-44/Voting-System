import tkinter as t
from tkinter import messagebox
import mysql.connector
import subprocess

# Create main window
root = t.Tk()
root.title("Voter Login - Voting System")
root.geometry("600x400")
root.configure(bg="lightgrey")

# Submit login credentials
def submit():
    useraadhar = taadhar.get()
    password = tpass.get()

    # Check if fields are empty
    if useraadhar == "" or password == "":
        messagebox.showwarning("Missing Fields", "Please fill in both Aadhar and Password.")
        return

    try:
        # Connect to MySQL
        db = mysql.connector.connect(host='localhost', user='root', password='', database='VotingSystem')
        cur = db.cursor()

        # Check user credentials
        q = "SELECT * FROM myuser WHERE aadhar = %s AND password = %s"
        v = (useraadhar, password)
        cur.execute(q, v)
        rec = cur.fetchall()

        if rec:
            messagebox.showinfo("Login Successful", "Welcome Voter! Proceed to Vote")
            root.destroy()
            subprocess.run(["python", "Home_page.py"]) #  Open voting page
        else:
            messagebox.showerror("Login Failed", "Invalid Aadhar or Password")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# --- UI --- #

# Heading
t.Label(root, text="Voter Login", font=('Monotype Corsiva', 24), bg="white").pack(pady=20)

# Aadhar Label & Entry
t.Label(root, text="Enter Aadhar Number", font=('Arial', 14), bg="lightgrey").pack(pady=5)
taadhar = t.Entry(root, font=('Arial', 16), width=30)
taadhar.pack(pady=5)

# Password Label & Entry
t.Label(root, text="Enter Password", font=('Arial', 14), bg="lightgrey").pack(pady=5)
tpass = t.Entry(root, font=('Arial', 16), width=30, show="*")
tpass.pack(pady=5)

# Submit Button
t.Button(root, text="LOGIN", font=('Arial', 18, 'bold'), bg='blue', fg='white', command=submit).pack(pady=30)

# Run app
root.mainloop()
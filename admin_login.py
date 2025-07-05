import tkinter as tk
from tkinter import messagebox

#Admin credentials
ADMIN_USERNAME = "Sujal Raja"
ADMIN_PASSWORD = "Sujal@123"

root = tk.Tk()
root.title("Admin Login")
root.geometry("500x300")
root.configure(bg="lightblue")

def login():
    uname = entry_username.get()
    passwd = entry_password.get()

    if not uname or not passwd:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    if uname == ADMIN_USERNAME and passwd == ADMIN_PASSWORD:
        messagebox.showinfo("Success", "Welcome Admin!")
        root.destroy()
        import EC_home
    else:
        messagebox.showerror("Access Denied", "Invalid username or password.")

# --- UI Design ---

tk.Label(root, text="Admin Login", font=('Arial', 20, 'bold'), bg="lightblue").pack(pady=20)

tk.Label(root, text="Username", font=('Arial', 14), bg="lightblue").pack(pady=5)
entry_username = tk.Entry(root, font=('Arial', 14), width=30)
entry_username.pack()

tk.Label(root, text="Password", font=('Arial', 14), bg="lightblue").pack(pady=5)
entry_password = tk.Entry(root, font=('Arial', 14), show='*', width=30)
entry_password.pack()

tk.Button(root, text="Login", font=('Arial', 14, 'bold'), bg='green', fg='white', command=login).pack(pady=20)

root.mainloop()

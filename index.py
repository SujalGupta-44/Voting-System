import tkinter as tk
from tkinter import font

# Root Window
root = tk.Tk()
root.title("Online Voting System")
root.geometry("600x400")
root.configure(bg="sky blue")

# Heading Label
heading = tk.Label(
    root,
    text="Online Voting System",
    font=('monotype corsiva', 28, 'bold'),
    bg="sky blue",
    fg="black"
)
heading.pack(pady=40)

# Function for admin button
def open_admin_login():
    print("Admin Login window opened.")
    import admin_login  

# Function for user button
def open_user_login():
    print("User Login window opened.")
    import user_login

def open_register():
    print("Registration Form opened.")
    import register 


# Buttons
btn_admin = tk.Button(
    root,
    text="Admin Login",
    font=('bell mt', 18, 'bold'),
    bg='white',
    fg='black',
    width=20,
    command=open_admin_login
)
btn_admin.pack(pady=10)

btn_user = tk.Button(
    root,
    text="User Login",
    font=('bell mt', 18, 'bold'),
    bg='white',
    fg='black',
    width=20,
    command=open_user_login
)
btn_user.pack(pady=10)# Click here to register (text link)
register_label = tk.Label(
    root,
    text="Click here to register",
    font=('Arial', 12, 'underline'),
    fg='blue',
    bg="sky blue",
    cursor="hand2"
)
register_label.pack()
register_label.bind("<Button-1>", lambda e: open_register())



root.mainloop()

import tkinter as t
from tkinter import messagebox
import mysql.connector

root = t.Tk()
root.title("Voting Machine")
root.geometry("800x700")
root.configure(bg="sky blue")

def submit():
    vote = var1.get()
    print("DEBUG: Selected vote:", vote)  # Debugging line

    if vote == "":
        messagebox.showwarning("No Selection", "Please select a party before submitting your vote.")
        return

    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='VotingSystem'
        )
        cur = db.cursor()

        # Ensure table exists with correct schema
        cur.execute('''
            CREATE TABLE IF NOT EXISTS votes (
                party_name VARCHAR(50) PRIMARY KEY,
                vote_count INT
            )
        ''')

        # Insert or update the vote
        cur.execute("SELECT vote_count FROM votes WHERE party_name = %s", (vote,))
        row = cur.fetchone()

        if row:
            cur.execute("UPDATE votes SET vote_count = vote_count + 1 WHERE party_name = %s", (vote,))
        else:
            cur.execute("INSERT INTO votes (party_name, vote_count) VALUES (%s, %s)", (vote, 1))

        db.commit()
        messagebox.showinfo("Vote Submitted", f"You voted for {vote}")
        root.destroy()
        

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# UI Header
lhead = t.Label(root, text="Vote for Your Party", font=("Monotype Corsiva", 24), bg="white")
lhead.pack(pady=20)

# Variable to store selected vote
var1 = t.StringVar(value="")  # Default is blank

# Parties List
parties = ['BJP', 'CONG', 'BSP', 'SP', 'AAP', 'TDP']

for party in parties:
    r = t.Radiobutton(
        root,
        text=party,
        variable=var1,
        value=party,
        font=("Arial", 16, "bold"),
        bg="white",
        width=20,
        indicatoron=0,
        selectcolor="lightgreen",
        activebackground="lightblue"
    )
    r.pack(pady=10)

submit = t.Button(root, text="SUBMIT VOTE", font=('Bell MT', 18, 'bold'), bg='green', fg='white', command=submit)
submit.pack(pady=30)

if __name__ == "__main__":
    root.mainloop()

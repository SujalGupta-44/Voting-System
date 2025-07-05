import tkinter as t
from tkinter import messagebox
import mysql.connector

# Create main window
root = t.Tk()
root.title("Election Result")
root.geometry("600x500")
root.configure(bg="lightyellow")

# Heading
t.Label(root, text="Election Results", font=('Monotype Corsiva', 24), bg="lightyellow").pack(pady=20)

# Frame to hold party results
frame = t.Frame(root, bg="white")
frame.pack(pady=20)

try:
    # Connect to database
    db = mysql.connector.connect(host='localhost', user='root', password='', database='VotingSystem')
    cur = db.cursor()

    # Fetch vote counts
    cur.execute("SELECT * FROM votes")
    records = cur.fetchall()

    if not records:
        t.Label(frame, text="No votes cast yet.", font=('Arial', 16), bg="white").pack(pady=10)
    else:
        max_votes = 0
        winner = ""

        for party, count in records:
            t.Label(frame, text=f"{party}: {count} votes", font=('Arial', 16), bg="white").pack(pady=5)

            if count > max_votes:
                max_votes = count
                winner = party

        t.Label(root, text=f"\n\n Winner: {winner} ", font=('Arial', 20, 'bold'), fg='green', bg="lightyellow").pack()

except Exception as e:
    messagebox.showerror("Database Error", str(e))


# RESET VOTES FUNCTION
def reset_votes():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to reset all votes?")
    if confirm:
        try:
            cur.execute("DELETE FROM votes")
            db.commit()
            messagebox.showinfo("Reset Done", "All votes have been reset successfully.")
            root.destroy()
            import EC_home  # reload updated page
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reset votes.\n{e}")

# RESET BUTTON
reset_btn = t.Button(root, text="Reset Votes", font=("Arial", 14, "bold"), bg="red", fg="white", command=reset_votes)
reset_btn.pack(pady=20)    

# Run app
root.mainloop()
import tkinter as tk
import random

# List of quotes (you can add more)
quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Don’t let yesterday take up too much of today.", "Will Rogers"),
    ("It’s not whether you get knocked down, it’s whether you get up.", "Vince Lombardi"),
    ("If you are working on something exciting, it will keep you motivated.", "Steve Jobs"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Believe you can and you’re halfway there.", "Theodore Roosevelt")
]

# Function to display a random quote
def show_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

# Create main window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")
root.config(bg="#f8f9fa")

# Quote label
quote_label = tk.Label(root, text="", wraplength=400, font=("Helvetica", 14, "italic"), bg="#f8f9fa", fg="#212529", justify="center")
quote_label.pack(pady=40)

# Author label
author_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f8f9fa", fg="#495057")
author_label.pack(pady=10)

# Button
new_quote_btn = tk.Button(root, text="New Quote", command=show_quote, font=("Helvetica", 12), bg="#007bff", fg="white", relief="flat", padx=10, pady=5)
new_quote_btn.pack(pady=20)

# Show initial quote
show_quote()

# Run the app
root.mainloop()
 
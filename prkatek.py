import tkinter as tk
from tkinter import ttk
app= tk.Tk()
app.configure(bg="pink")
app.geometry("400x300")
app.title("project")

input_frame = ttk.Frame(app)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

nama_depan_label = ttk.Label(app,text="nayy")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True)

app.mainloop()

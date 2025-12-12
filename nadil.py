import tkinter as tk
from tkinter import messagebox

# ------------------ FUNGSI ------------------
def buka_form():
    menu_frame.pack_forget()
    form_frame.pack(fill="both", expand=True)

def kembali_ke_menu():
    form_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)

def simpan_data():
    nama = entry_nama.get()
    nim = entry_nim.get()

    if nama == "" or nim == "":
        messagebox.showwarning("Peringatan", "Nama dan NIM tidak boleh kosong!")
    else:
        messagebox.showinfo("Data Tersimpan", f"Nama: {nama}\nNIM: {nim}")

# ------------------ GUI ------------------
root = tk.Tk()
root.title("Input Nama & NIM - Pink Theme")
root.geometry("330x300")
root.configure(bg="#FFD6E8")   # Pink lembut

# ------------------ MENU FRAME ------------------
menu_frame = tk.Frame(root, bg="#FFD6E8")

menu_label = tk.Label(menu_frame, text="Menu Utama", 
                      font=("Arial", 18, "bold"), 
                      bg="#FFD6E8", fg="#FF4D8D")

menu_button = tk.Button(menu_frame, text="Mulai Isi Data",
                        font=("Arial", 12),
                        bg="#FF9EC7", fg="white",
                        activebackground="#FF7BBF",
                        width=15,
                        command=buka_form)

menu_label.pack(pady=30)
menu_button.pack(pady=10)
menu_frame.pack(fill="both", expand=True)

# ------------------ FORM FRAME ------------------
form_frame = tk.Frame(root, bg="#FFEBF5")

label_nama = tk.Label(form_frame, text="Masukkan Nama:",
                      bg="#FFEBF5", fg="#C2185B", font=("Arial", 12))
entry_nama = tk.Entry(form_frame, bg="#FFE3EE", fg="black", width=25)

label_nim = tk.Label(form_frame, text="Masukkan NIM:",
                     bg="#FFEBF5", fg="#C2185B", font=("Arial", 12))
entry_nim = tk.Entry(form_frame, bg="#FFE3EE", fg="black", width=25)

button_simpan = tk.Button(form_frame, text="Simpan",
                          bg="#FF8BB5", fg="white",
                          activebackground="#FF6DAA",
                          width=10,
                          command=simpan_data)

button_kembali = tk.Button(form_frame, text="Kembali",
                           bg="#FFB6D9", fg="white",
                           activebackground="#FFA0CF",
                           width=10,
                           command=kembali_ke_menu)

label_nama.pack(pady=5)
entry_nama.pack(pady=5)
label_nim.pack(pady=5)
entry_nim.pack(pady=5)
button_simpan.pack(pady=10)
button_kembali.pack(pady=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

FILE_NAME = "belanja.txt"

# -------- Function Utama ---------
def tambah_barang(nama, jumlah):
    if nama == "" or jumlah == "":
        return False
    try:
        jumlah = int(jumlah)
        with open(FILE_NAME, "a") as file:
            file.write(f"{nama}-{jumlah}\n")
        return True
    except ValueError:
        return False

def baca_daftar():
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def hapus_barang(nama):
    data = baca_daftar()
    new_data = [item for item in data if not item.startswith(nama + "-")]
    with open(FILE_NAME, "w") as file:
        file.writelines(new_data)
    return len(data) != len(new_data)

def reset():
    open(FILE_NAME, "w").close()


# -------- GUI --------
root = tk.Tk()
root.title("To-Do List Belanjaan")
root.geometry("380x450")
root.configure(bg="navy")

tk.Label(root, text="Nama Barang:").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="Jumlah:").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

def tambah():
    nama = entry_nama.get()
    jumlah = entry_jumlah.get()
    if tambah_barang(nama, jumlah):
        messagebox.showinfo("Sukses", "Barang ditambahkan!")
        entry_nama.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Isi nama dan jumlah (jumlah harus angka)")

def lihat():
    data = baca_daftar()
    if not data:
        messagebox.showinfo("Daftar Belanja", " belum ada barang yang di tambahkan")
        return
    daftar = ""
    for i in data:
        daftar += i
    messagebox.showinfo("Daftar Belanja", daftar)

def hapus():
    nama = entry_nama.get()
    if nama == "":
        messagebox.showerror("Error", "Masukkan nama barang yang ingin dihapus")
        return
    if hapus_barang(nama):
        messagebox.showinfo("Sukses", f"{nama} berhasil dihapus")
    else:
        messagebox.showwarning("Info", "Barang tidak ditemukan")

def hapus_semua():
    reset()
    messagebox.showinfo("Sukses", "Semua daftar belanja dihapus!")

tk.Button(root, text="Tambah Barang", command=tambah).pack(pady=4)
tk.Button(root, text="Lihat Daftar", command=lihat).pack(pady=4)
tk.Button(root, text="Hapus Barang", command=hapus).pack(pady=4)
tk.Button(root, text="Reset Daftar Belanja", command=hapus_semua).pack(pady=4)
tk.Button(root, text="Keluar", command=root.quit).pack(pady=8)

root.mainloop()
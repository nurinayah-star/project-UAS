import tkinter as tk
from tkinter import ttk, messagebox, StringVar
import os

#----------------------WINDOW LOGIN
login = tk.Tk()
login.geometry('350x400')
login.resizable(False, False)
login.title("LOGIN ADMIN")
login.configure(background="#B1B1B1")

#----------------------STYLE & KONFIGURASI
style = ttk.Style()
style.theme_use('clam')
style.configure(background="#391E10", foreground="white")
style.configure("submit_btn.TButton", font=('calibri', 10, 'bold'))
style.configure("Treeview", font=('calibri', 10), rowheight=25)
style.configure("Treeview.Heading", font=('calibri', 11, 'bold'))

USERNAME = StringVar()
PASSWORD = StringVar()
FILE_MEMBER = "data_member.txt"

#-----------------------Fungsi Login
def masuk():
    user = USERNAME.get()
    pw = PASSWORD.get()

    if user == "" or pw == "":
        messagebox.showerror("Error", "Data nya ngga boleh kosong yaa!😊")
        return

    if user == "remajajompo" and pw == "123":
        login.destroy()
        buka_kelola_member()
    else:
        messagebox.showerror("Gagal Login", "Waduh.. Username / password kamu salah")

#-----------------------LAYOUT LOGIN
tk.Label(login, text="LOGIN ADMIN", bg="#391E10", fg="white",
         font=('calibri', 16, 'bold')).pack(pady=10)
ttk.Label(login, text="Silahkan Masuk", style="white.TLabel").pack()

frame_log = ttk.Frame(login)
frame_log.pack(pady=15, padx=20, fill='x')

ttk.Label(frame_log, text="👤 Username:", style="white.TLabel").pack(anchor="w")
ttk.Entry(frame_log, textvariable=USERNAME).pack(fill='x')
ttk.Label(frame_log, text="🔑 Password:", style="white.TLabel").pack(anchor="w", pady=(10,0))
ttk.Entry(frame_log, textvariable=PASSWORD, show="*").pack(fill='x')
ttk.Button(frame_log, text="MASUK", style="submit_btn.TButton", command=masuk).pack(pady=20, fill='x')

ttk.Label(login, text='More Info: @_inayaa.h | @nufdhmn', background="#B1B1B1").pack(side='bottom', pady=10)


#---------------------------------------------------------
#       FUNGSI UTAMA (KELOLA MEMBER)
#---------------------------------------------------------
def buka_kelola_member():
    gui = tk.Tk()
    gui.geometry('650x600') # Diperlebar agar tabel muat
    gui.resizable(False, False)
    gui.title("KELOLA DATA MEMBER")
    gui.configure(background='#B1B1B1')

    # --- Variables ---
    NAMA = StringVar()
    UMUR = StringVar()
    JENIS_KELAMIN = StringVar()
    AGAMA = StringVar()

    # --- Helper: Baca & Tulis File ---
    def baca_data():
        if not os.path.exists(FILE_MEMBER):
            return []
        with open(FILE_MEMBER, "r") as f:
            lines = f.readlines()
        data = []
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 4: # Pastikan data lengkap
                data.append(parts)
        return data

    def simpan_semua_data(data_list):
        with open(FILE_MEMBER, "w") as f:
            for item in data_list:
                f.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")

    def refresh_tabel():
        # Hapus data lama di tabel GUI
        for item in tabel.get_children():
            tabel.delete(item)
        # Ambil data baru dari file
        data = baca_data()
        for i, row in enumerate(data):
            # iid=i penting untuk mengenali nomor baris saat update/hapus
            tabel.insert("", "end", iid=i, values=(row[0], row[1], row[2], row[3]))

    def clear_form():
        NAMA.set("")
        UMUR.set("")
        JENIS_KELAMIN.set("")
        AGAMA.set("")
        # Hilangkan seleksi di tabel
        if tabel.selection():
            tabel.selection_remove(tabel.selection())

    # --- FUNGSI CRUD (Create, Read, Update, Delete) ---

    # 1. TAMBAH MEMBER
    def tambah_member():
        nama = NAMA.get()
        umur = UMUR.get()
        jk = JENIS_KELAMIN.get()
        agama = AGAMA.get()

        if nama == "" or umur == "" or jk == "" or agama == "":
            messagebox.showwarning("Perhatian", "Semua data wajib diisi!")
            return
        if not umur.isdigit():
            messagebox.showerror("Error", "Umur harus angka!")
            return

        with open(FILE_MEMBER, "a") as file:
            file.write(f"{nama},{umur},{jk},{agama}\n")
        
        messagebox.showinfo("Sukses", "Member berhasil ditambahkan!")
        clear_form()
        refresh_tabel()

    # 2. HAPUS MEMBER
    def hapus_member():
        selected = tabel.selection()
        if not selected:
            messagebox.showwarning("Pilih Data", "Klik dulu nama member di tabel yang mau dihapus!")
            return
        
        confirm = messagebox.askyesno("Konfirmasi", "Yakin mau menghapus member ini?")
        if confirm:
            index = int(selected[0]) # Ambil index baris
            data = baca_data()
            del data[index] # Hapus dari list
            simpan_semua_data(data) # Tulis ulang file
            refresh_tabel()
            clear_form()
            messagebox.showinfo("Terhapus", "Data member berhasil dihapus.")

    # 3. UPDATE MEMBER
    def update_member():
        selected = tabel.selection()
        if not selected:
            messagebox.showwarning("Pilih Data", "Klik dulu member di tabel yang mau diedit!")
            return
        
        nama = NAMA.get()
        umur = UMUR.get()
        jk = JENIS_KELAMIN.get()
        agama = AGAMA.get()

        if nama == "" or umur == "":
             messagebox.showwarning("Gagal", "Data tidak boleh kosong saat update!")
             return

        index = int(selected[0])
        data = baca_data()
        
        # Timpa data lama dengan yang baru di inputan
        data[index] = [nama, umur, jk, agama]
        
        simpan_semua_data(data)
        refresh_tabel()
        clear_form()
        messagebox.showinfo("Update", "Data member berhasil diperbarui!")

    # 4. LIHAT KARTU MEMBER
    def lihat_kartu():
        selected = tabel.selection()
        # Jika user tidak memilih tabel, tapi sudah isi form, kita pakai data form
        # Tapi lebih aman pakai data dari tabel agar valid
        
        nama_k = NAMA.get()
        umur_k = UMUR.get()
        jk_k = JENIS_KELAMIN.get()
        agama_k = AGAMA.get()

        if nama_k == "":
            messagebox.showwarning("Info", "Pilih data member di tabel dulu, atau isi form!")
            return

        # Pop up Kartu
        gui2 = tk.Toplevel()
        gui2.title("KARTU MEMBER")
        gui2.geometry("450x280")
        gui2.configure(background='#B1B1B1')
        gui2.resizable(False, False)

        frame_kartu = ttk.Frame(gui2)
        frame_kartu.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame_kartu, text="KARTU MEMBER MINI-MARKET",
                  font=('calibri', 14, 'bold')).pack(pady=(0,10))
        ttk.Label(frame_kartu, text="----------------------------------").pack()
        ttk.Label(frame_kartu, text=f"Nama  : {nama_k}", font=('calibri', 12)).pack(anchor='w', padx=50)
        ttk.Label(frame_kartu, text=f"Umur  : {umur_k} Tahun", font=('calibri', 12)).pack(anchor='w', padx=50)
        ttk.Label(frame_kartu, text=f"Gender: {jk_k}", font=('calibri', 12)).pack(anchor='w', padx=50)
        ttk.Label(frame_kartu, text=f"Agama : {agama_k}", font=('calibri', 12)).pack(anchor='w', padx=50)
        ttk.Label(frame_kartu, text="----------------------------------").pack()
        ttk.Label(frame_kartu, text="*Berlaku Selamanya", font=('calibri', 8, 'italic')).pack(pady=10)

    # --- Event Handler ---
    def pilih_baris(event):
        # Saat baris tabel diklik, isi form input otomatis (agar siap diedit/dilihat)
        selected = tabel.selection()
        if selected:
            values = tabel.item(selected)['values']
            # Masukkan ke variable StringVar
            NAMA.set(values[0])
            UMUR.set(values[1])
            JENIS_KELAMIN.set(values[2])
            AGAMA.set(values[3])

    # ------------ GUI LAYOUT ------------
    
    # 1. Header
    ttk.Label(gui, text="KELOLA DATA MEMBER", foreground="white", background="#391E10",
            font=('calibri', 18, 'bold')).pack(pady=10, fill='x')

    # 2. Form Input
    frame_input = ttk.LabelFrame(gui, text=" Form Data ", labelanchor='n')
    frame_input.pack(padx=20, pady=5, fill='x')

    # Grid Layout untuk Input
    ttk.Label(frame_input, text="Nama:", background="#B1B1B1").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_input, textvariable=NAMA, width=30).grid(row=0, column=1, padx=10)

    ttk.Label(frame_input, text="Umur:", background="#B1B1B1").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_input, textvariable=UMUR, width=30).grid(row=1, column=1, padx=10)
    
    ttk.Label(frame_input, text="Gender:", background="#B1B1B1").grid(row=2, column=0, sticky='w', padx=10, pady=5)
    # Gunakan Combobox biar rapi untuk gender
    combo_jk = ttk.Combobox(frame_input, textvariable=JENIS_KELAMIN, width=27, state="readonly")
    combo_jk['values'] = ('Laki-laki', 'Perempuan')
    combo_jk.grid(row=2, column=1, padx=10)
    
    ttk.Label(frame_input, text="Agama:", background="#B1B1B1").grid(row=3, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_input, textvariable=AGAMA, width=30).grid(row=3, column=1, padx=10)

    # 3. Tombol Menu (CRUD)
    frame_btn = ttk.Frame(gui)
    frame_btn.pack(pady=10)

    ttk.Button(frame_btn, text="SIMPAN BARU", command=tambah_member).grid(row=0, column=0, padx=5)
    ttk.Button(frame_btn, text="UPDATE DATA", command=update_member).grid(row=0, column=1, padx=5)
    ttk.Button(frame_btn, text="HAPUS DATA", command=hapus_member).grid(row=0, column=2, padx=5)
    ttk.Button(frame_btn, text="LIHAT KARTU", command=lihat_kartu).grid(row=0, column=3, padx=5)
    ttk.Button(frame_btn, text="RESET FORM", command=clear_form).grid(row=0, column=4, padx=5)

    # 4. Tabel Data (Treeview)
    frame_tabel = ttk.Frame(gui)
    frame_tabel.pack(padx=20, pady=5, fill='both', expand=True)

    cols = ('nama', 'umur', 'jk', 'agama')
    tabel = ttk.Treeview(frame_tabel, columns=cols, show='headings', height=8)
    
    tabel.heading('nama', text='Nama Lengkap')
    tabel.heading('umur', text='Umur')
    tabel.heading('jk', text='Jenis Kelamin')
    tabel.heading('agama', text='Agama')

    tabel.column('nama', width=150)
    tabel.column('umur', width=50, anchor='center')
    tabel.column('jk', width=100)
    tabel.column('agama', width=100)

    # Scrollbar untuk tabel
    scroll = ttk.Scrollbar(frame_tabel, orient="vertical", command=tabel.yview)
    tabel.configure(yscroll=scroll.set)
    
    tabel.pack(side='left', fill='both', expand=True)
    scroll.pack(side='right', fill='y')

    # Bind event klik
    tabel.bind('<<TreeviewSelect>>', pilih_baris)



    gui.mainloop()

login.mainloop()
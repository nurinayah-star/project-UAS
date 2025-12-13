import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar
import random

#----------------------WINDOW LOGIN
login = tk.Tk()
login.geometry('350x400')
login.resizable(False,False )
login.title("LOGIN MEMBER MINI MARKET")
login.configure(background="#B1B1B1")

#----------------------STYLE
style = ttk.Style()
style.configure("white.TLabel",background="#2E1E2B", foreground='white')
style.configure("submit_btn.TButton", font=('calibri', 11, 'bold'))
label_info = ttk.Label(text='More Info: @ith.campus | @pmb_ith',style="frame_label.TLabel")
label_info.pack(padx=10,fill='y')

USERNAME = StringVar()
PASSWORD = StringVar()

def masuk():
    user = USERNAME.get()
    pw = PASSWORD.get()

    if user == "" or pw == "":
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return

    if user == "remajajompo" and pw == "123":
        login.destroy()
        buka_form_member()
    else:
        messagebox.showerror("Gagal Login", "Username / password salah!")

ttk.Label(login, text="LOGIN", style="white.TLabel", font=('calibri', 16, 'bold')).pack(pady=10)
ttk.Label(login, text="Masukkan akun kamu", style="white.TLabel").pack()

frame_log = ttk.Frame(login)
frame_log.pack(pady=15, padx=20, fill='x')
ttk.Label(frame_log, text="Username:", style="white.TLabel").pack(anchor="w")
ttk.Entry(frame_log, textvariable=USERNAME).pack(fill='x')
ttk.Label(frame_log, text="Password:", style="white.TLabel").pack(anchor="w", pady=(10,0))
ttk.Entry(frame_log, textvariable=PASSWORD, show="*").pack(fill='x')
ttk.Button(frame_log, text="MASUK", style="submit_btn.TButton", command=masuk).pack(pady=20, fill='x')

#----------------------FORM UTAMA MEMBER

def buka_form_member():
    gui = tk.Tk()
    gui.geometry('400x500')
    gui.resizable(False, False)
    gui.title("MEMBER MINI MARKET")
    gui.configure(background='#1E1E2E')

    # ----------------------VARIABLES
    NAMA = StringVar()
    UMUR = StringVar()
    JENIS_KELAMIN= StringVar()
    AGAMA=StringVar()

    # ----------------------Fungsi Submit
    def buka_kartu():
        nama = NAMA.get()
        umur = UMUR.get()
        jenis_kelamin = JENIS_KELAMIN.get()
        agama = AGAMA.get()
    

        #----------------------ERROR HANDLING
        if nama == "" or umur == "" or jenis_kelamin ==""or agama =="":
            messagebox.showwarning("Perhatian", "Semua data wajib diisi!")
            return

        if not umur.isdigit():
            messagebox.showerror("Error", "Umur harus angka!")
            return

        #----------------------Simpan ke TXT
        try:
            with open("data_member.txt", "a") as file:
                file.write(f"{nama},{umur},{jenis_kelamin},{agama}\n")
        except:
            messagebox.showerror("File Error", "Gagal menyimpan data ke file!")
            return

        gui2 = tk.Toplevel()
        gui2.title("KARTU MEMBER")
        gui2.geometry("450x280")
        gui2.configure(background='#1E1E2E')
        gui2.resizable(False, False)

        #----------------------Kartu
        frame = ttk.Frame(gui2)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        label_info = ttk.Label(text='More Info: @ith.campus | @pmb_ith',style="frame_label.TLabel")
        label_info.pack(padx=10,fill='y')
        ttk.Label(frame, text="KARTU MEMBER MINI-MARKET", font=('calibri', 14, 'bold')).pack(pady=10)
        ttk.Label(frame, text=f"Nama   : {nama}", font=('calibri', 12)).pack()
        ttk.Label(frame, text=f"Umur   : {umur}", font=('calibri', 12)).pack()
        ttk.Label(frame, text=f"Umur   : {jenis_kelamin}", font=('calibri', 12)).pack()
        ttk.Label(frame, text=f"Umur   : {agama}", font=('calibri', 12)).pack()

    #----------------------GUI UTAMA
    ttk.Label(gui, text="DAFTAR MEMBER", foreground="white", background="#1E1E2E",
              font=('calibri', 16, 'bold')).pack(pady=10)
    ttk.Label(gui, text="Masukkan data kamu", foreground="white", background="#1E1E2E",
              font=('calibri', 12)).pack()
    
    frame_input = ttk.Frame(gui)
    frame_input.pack(padx=25, pady=20, fill='both', expand=True)
    #----------------------LABEL UNTUK NAMA
    ttk.Label(frame_input, text="Nama:", foreground="white", background="#1E1E2E").pack(anchor="w")
    ttk.Entry(frame_input, textvariable=NAMA).pack(fill='x')
    #----------------------LABEL UNTUK UMUR
    ttk.Label(frame_input, text="Umur:", foreground="white", background="#1E1E2E").pack(anchor="w", pady=(10,0))
    ttk.Entry(frame_input, textvariable=UMUR).pack(fill='x')
     #----------------------LABEL UNTUK JENIS_KELAMIN
    ttk.Label(frame_input, text="Jenis_Kelamin:", foreground="white", background="#1E1E2E").pack(anchor="w", pady=(10,0))
    ttk.Entry(frame_input, textvariable=JENIS_KELAMIN).pack(fill='x')
     #----------------------LABEL UNTUK AGAMA
    ttk.Label(frame_input, text="Agama:", foreground="white", background="#1E1E2E").pack(anchor="w", pady=(10,0))
    ttk.Entry(frame_input, textvariable=AGAMA).pack(fill='x')
     #----------------------TOMBOL CETAK KARTU MEMBER
    ttk.Button(frame_input, text="Buat Kartu Member", style="submit_btn.TButton",
               command=buka_kartu).pack(pady=20, fill='x')

    label_info = ttk.Label(text='More Info: @ith.campus | @pmb_ith',style="frame_label.TLabel")
    label_info.pack(padx=10,fill='y')
    gui.mainloop()

login.mainloop()
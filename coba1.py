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
style.configure("white.TLabel",background="#391E10", foreground='white')
style.configure("submit_btn.TButton", font=('calibri', 11, 'bold'))
label_info = ttk.Label(text='More Info: @_inayaa.h | @nufdhmn', style="frame_label.TLabel")
label_info.pack(pady=5)


USERNAME = StringVar()
PASSWORD = StringVar()

#-----------------------Fungsi Submit
def masuk():
    user = USERNAME.get()
    pw = PASSWORD.get()

#-----------------------Error Handling
    if user == "" or pw == "":
        messagebox.showerror("Error", "data nya ngga boleh kosong yaa!😊")
        return

    if user == "remajajompo" and pw == "123":
            login.destroy()
            buka_form_member()

    else:
        messagebox.showerror("Gagal Login", "Waduh.. Username / password kamu salah")
def lihat_member():
    win = tk.Toplevel()
    win.title("Daftar Member")
    win.geometry("400x300")

    text = tk.Text(win)
    text.pack(fill='both', expand=True)

    try:
        with open("data_member.txt", "r") as file:
            data = file.read()
            text.insert("end", data if data else "Belum ada member.")
    except:
        text.insert("end", "File tidak ditemukan.")
def buka_form_member():
    gui = tk.Tk()
    gui.geometry("400x520")
    gui.title("MEMBER MINI MARKET")

    # ===== MENU BAR =====
    menu_bar = tk.Menu(gui)
    gui.config(menu=menu_bar)

    menu_member = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Menu Member", menu=menu_member)

    menu_member.add_command(label="Lihat Daftar Member", command=lihat_member)
    menu_member.add_command(label="Hapus Member", command=hapus_member)
    menu_member.add_command(label="Update Member", command=update_member)
    menu_member.add_separator()
    menu_member.add_command(label="Keluar", command=gui.destroy)

tk.Label(login, text="LOGIN", bg="#391E10", fg="white",
         font=('calibri', 16, 'bold')).pack(pady=10)
ttk.Label(login, text="Masukkan akun kamu", style="white.TLabel").pack()


frame_log = ttk.Frame(login)
frame_log.pack(pady=5, padx=10, fill='x')
frame_log.pack(pady=15, padx=20, fill='x')

ttk.Label(frame_log, text="👤 Username:", style="white.TLabel").pack(anchor="w")
ttk.Entry(frame_log, textvariable=USERNAME).pack(fill='x')
ttk.Label(frame_log, text="🔑 Password:", style="white.TLabel").pack(anchor="w", pady=(10,0))
ttk.Entry(frame_log, textvariable=PASSWORD, show="*").pack(fill='x')
ttk.Button(frame_log, text="MASUK", style="submit_btn.TButton", command=masuk).pack(pady=20, fill='x')

#----------------------FORM UTAMA MEMBER

def buka_form_member():
    gui = tk.Tk()
    gui.geometry('400x400')
    gui.resizable(False, False)
    gui.title("MEMBER MINI MARKET")
    gui.configure(background='#B1B1B1')
    gui.configure(background="#B1B1B1")

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
        gui2.configure(background='#B1B1B1')
        gui2.resizable(False, False)

        #----------------------Kartu
        frame = ttk.Frame(gui2)

        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="KARTU MEMBER MINI-MARKET",
          font=('calibri', 14, 'bold')).pack()

        ttk.Label(frame, text=f"Nama : {nama}", font=('calibri', 12)).pack()
        ttk.Label(frame, text=f"Umur : {umur}", font=('calibri', 12)).pack()
        ttk.Label(frame, text=f"Jenis Kelamin : {jenis_kelamin}", font=('calibri', 12)).pack()

        ttk.Label(frame, text=f"Agama : {agama}", font=('calibri', 12)).pack()


   
    # ------------ GUI UTAMA ------------
    ttk.Label(gui, text="DAFTAR MEMBER", foreground="white", background="#391E10",
            font=('calibri', 16, 'bold')).pack(pady=10)
    ttk.Label(gui, text="Masukkan data kamu", foreground="white", background="#391E10",
              font=('calibri', 12)).pack()
    
    frame_input = ttk.Frame(gui)
    frame_input.pack(padx=25, pady=20, fill='both', expand=True)
    #----------------------LABEL UNTUK NAMA
    ttk.Label(frame_input, text="Nama:", foreground="white", background="#391E10").pack(anchor="w")
    ttk.Entry(frame_input, textvariable=NAMA).pack(fill='x')
    #----------------------LABEL UNTUK UMUR
    ttk.Label(frame_input, text="Umur:", foreground="white", background="#391E10").pack(anchor="w", pady=(8,0))
    ttk.Entry(frame_input, textvariable=UMUR).pack(fill='x')
     #----------------------LABEL UNTUK JENIS_KELAMIN
    ttk.Label(frame_input, text="Jenis_Kelamin:", foreground="white", background="#391E10").pack(anchor="w", pady=(8,0))
    ttk.Entry(frame_input, textvariable=JENIS_KELAMIN).pack(fill='x')
     #----------------------LABEL UNTUK AGAMA
    ttk.Label(frame_input, text="Agama:", foreground="white", background="#391E10").pack(anchor="w", pady=(8,0))
    ttk.Entry(frame_input, textvariable=AGAMA).pack(fill='x')
     #----------------------TOMBOL CETAK KARTU MEMBER
    ttk.Button(frame_input, text="Buat Kartu Member", style="submit_btn.TButton",
               command=buka_kartu).pack(pady=20, fill='x')

    label_info = ttk.Label(text='More Info: @_inayaa.h | @nufdhmn',style="frame_label.TLabel")
    label_info.pack(padx=10,fill='y')

    gui.mainloop()

login.mainloop()
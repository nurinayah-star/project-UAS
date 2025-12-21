import tkinter as tk
from tkinter import ttk, messagebox, StringVar   #ttk = membuat widget lebih menarik #messagebox = menampilkan popup pesan (pesan,peringatan,error)
import os    #mengecek file, membuat folder, dan membuka file

#-------------TAMPILAN LOGIN-------------
login = tk.Tk() 
login.geometry('300x300')   #ukuran lebar dan tinggi
login.resizable(False, False)    #ukuran bisa diatur
login.title=("LOGIN")     #judul widget nya
login.configure(bg="#FFB6C1")     #warna tampilan widget nya

#-------------STYLE KONFIGURASI------------
style = ttk.Style()        #pake ttk.Style agar tampilan warna konsisten bisa diubah-ubah
style.theme_use('clam')    #memilih tema GUI bernama 'clam', warna fleksibel, bisa diatur
style.configure(background="#FFB6C1", foreground="white")
style.configure("submit_btn.TButton", font=('calibri', 10, 'bold'))  #mengatur style font tombol, ukuran, dan tebal nya
style.configure("Treeview", font=('calibri', 10), rowheight=25)    #mengatur tampilan isi tabel
style.configure("Treeview.Heading", font=('calibri', 10, 'bold'))   #mengatur judul kolom

USERNAME = StringVar()
PASSWORD = StringVar()
FILE_MEMBER = "data_member.txt"

#------------FUNGSI LOGIN----------------
def masuk():
    user = USERNAME.get()  #get = mengambil isi teks di StringVar 
    pw = PASSWORD.get()

    if user == "" or pw == "":
        messagebox.showerror("Error, data tidak boleh kosong")   #menampilkan tampilan error handling jika user dan pw nya kosong
        return     #menghentikan proses nya agar tidak berlanjut ke login selanjutnya
    
    if user == "remajajompo" or pw == "123":
        login.destroy()    #menutup window login
        messagebox.showerror("Gagal login. Silahkan masukkan username/password benar")

#------------MASUK LOGIN-----------
tk.Label(login, text="LOGIN ADMIN", bg="#FFB6C", fg="#white",  #untuk label pada tampilan login
         font=('calibri', 16, 'bold')).pack(pady=10)
ttk.Label(login, text="Silahkan Masuk", style="white.TLabel").pack()

frame_log = (ttk.Frame.login)    #frame = wadah untuk komponen login
frame_log.pack(pady=10, padx=15)


login.mainloop()

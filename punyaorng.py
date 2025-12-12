import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

gui = tk.Tk()
gui.geometry('400x350')
gui.resizable(False, False)
gui.title("TAMPILAN LOGIN")
gui.configure(background='#072541')



# style untuk tampilan GUI-------------------
style = ttk.Style()
style.configure("gaya_label.TLabel",background='#072541',foreground='white',)
style.configure("frame_label.TLabel",background='white')
style.configure("frame_label.TFrame",background='white')
style.configure("button_submit.TButton",background='#00A9FF',foreground='black',font=('calibri',12 ))
style.configure("style_label2.TLabel",background='#072541',foreground='white',)
#------------------------------------------------------------------------


#------------------------------------------------------------------------ Label LOGIN
label_login = ttk.Label(gui,text='SILAHKAN LOGIN',style="gaya_label.TLabel" ,font=('calibri', 15, 'bold'))
label_login.pack(padx=80, pady=5, fill='y', expand=True)

label_login2 = ttk.Label(gui, text='Masukkan data anda dengan benar!',style="gaya_label.TLabel" ,font=('calibri', 12))
label_login2.pack()
#------------------------------------------------------------------------

#-------- Variabel untuk menyimpan data pengguna
NAMA_MAHASISWA = StringVar()
NAMA_PRODI = StringVar()
NIM_MAHASISWA = StringVar()
logo_image = None
#--------------------------------GUI ke 2
def data_mahasiswa(): # Fungsi ketika tekan Tombol SUBMIT
    NAMA_MAHASISWA.set(entry_nama.get())
    NAMA_PRODI.set(entry_prodi.get())
    NIM_MAHASISWA.set(entry_nim.get())
    #global logo_image
    #logo_ith = "C:\\Users\\User\\OneDrive\\Gambar\\Saved Pictures\\ith2.png" #file gambar
    #logo = Image.open(logo_ith)
    #logo = logo.resize((120, 50))
    #logo = ImageTk.PhotoImage(logo)

    gui2 = tk.Toplevel()
    gui2.geometry("450x280")
    gui2.title('TANDA PENGENAL MAHASISWA')
    gui2.configure(background='#072541')
    gui2.resizable(False,False)
   
    
    #---------------------------------------- Frame label
    frame_label2 = ttk.Label(gui2,style="frame_label.TLabel")
    frame_label2.pack(padx=10,pady=10,fill='y',expand=False)
    #---------------------------------------- Logo ITH
    #image_label = ttk.Label(frame_label2, image=logo,style="frame_label.TLabel")
    #image_label.image = logo  # Penting agar gambar tidak dihapus oleh garbage collector
    #image_label.pack(pady=2)
    #---------------------------------------- Label INFO 
    label_alamat = ttk.Label(frame_label2,text='Jl. Pemuda No. 6 Parepare, Sulawesi Selatan',style="frame_label.TLabel")
    label_alamat.pack(padx=98,pady=2,fill='y')
    label_info = ttk.Label(frame_label2,text='More Info: @ith.campus | @pmb_ith',style="frame_label.TLabel")
    label_info.pack(padx=10,fill='y')
    #----------------------------------------
    
    #---------------------------------------- Label GUI 2, NAMA,NIM,PRODI
    label_kartu = ttk.Label(gui2,text='KARTU TANDA MAHASISWA',style="gaya_label.TLabel" ,font=('calibri' ,15, 'bold'))
    label_prodi2 = ttk.Label(gui2, text=f'PRODI : {NAMA_PRODI.get().upper()}',style="style_label2.TLabel",font=('calibri', 12,'bold'))
    label_nim2 = ttk.Label(gui2, text=f'NIM     : {NIM_MAHASISWA.get()}',style="style_label2.TLabel",font=('calibri',12 ,'bold'))
    label_nama2 = ttk.Label(gui2, text=f'NAMA : {NAMA_MAHASISWA.get().upper()}',style="style_label2.TLabel",font=('calibri',12 ,'bold'))
    #----------------------------------------

    #----------------------------------------pemanggilan label NAMA,NIM,PRODI pada GUI2
    label_kartu.pack(fill='y',expand=None)
    label_prodi2.pack(padx=10,pady=10,fill='x',side='bottom',expand=None)
    label_nim2.pack(padx=10,pady=15,fill='x',side='bottom',expand=None)
    label_nama2.pack(padx=10,pady=5,fill='x',side='bottom',expand=None)
    #----------------------------------------
    
#-----------------------------
# gui pertama
#----------------------------- Frame label Untuk GUI 1
frame_label = ttk.Label(gui,style="frame_label.TFrame")
frame_label.pack(padx=60, pady=25, fill='both', expand=True)
#-----------------------------

#----------------------------- LABEL DAN INPUT NAMA
label_nama = ttk.Label(frame_label,style="frame_label.TLabel" ,text='NAMA:')
label_nama.pack(padx=10, pady=5, fill='x', expand=True)

entry_nama = ttk.Entry(frame_label, textvariable=NAMA_MAHASISWA)
entry_nama.pack(padx=35, fill='x', expand=True)
#----------------------------- LABEL DAN INPUT PRODI
label_prodi = ttk.Label(frame_label,style="frame_label.TLabel", text='PRODI:',)
label_prodi.pack(padx=10, pady=5, fill='x', expand=True)

entry_prodi = ttk.Entry(frame_label, textvariable=NAMA_PRODI)
entry_prodi.pack(padx=35, pady=5, fill='x', expand=True)
#----------------------------- LABEL DAN INPUT NIM
label_nim = ttk.Label(frame_label,style="frame_label.TLabel" ,text='NIM:')
label_nim.pack(padx=10, pady=5, fill='x', expand=True)

entry_nim = ttk.Entry(frame_label,textvariable=NIM_MAHASISWA)
entry_nim.pack(padx=35, pady=5, fill='x', expand=True)
#----------------------------- TOMBOL SUBMIT
button_submit = ttk.Button(frame_label,style="button_submit.TButton" ,text='SUBMIT',command=data_mahasiswa)
button_submit.pack(padx=100, pady=20, fill='x', expand=True)

# Main loop
gui.mainloop()
import sqlite3
import tkinter.messagebox
data = []
class aplikasi_pembelian():
    def __init__(self):
        self.jendela = tkinter.Tk()
        self.jendela.title('KASIR V.1.0')
        self.jendela.geometry('550x550')
        self.jendela.config(bg='gray')
        #toolbar
        self.frame_header = tkinter.Frame(self.jendela,bg='#282e28')
        self.tentang = tkinter.Button(self.frame_header,text='About',width=10,bg='#282e28',fg='#ffffff',relief='flat',command=self.biodata)
        self.help = tkinter.Button(self.frame_header,text='Help',width=10,bg='#282e28',fg='#ffffff',relief='flat')
        self.option = tkinter.Button(self.frame_header,text='Acount',width=10,bg='#282e28',fg='#ffffff',relief='flat',command=self.pengaturan)
        self.panjang = tkinter.Label(self.frame_header,text='',bg='#282e28',width=50)
        self.tentang.pack(side='left')
        self.help.pack(side='left')
        self.option.pack(side='left')
        self.option.pack(side='left')
        self.panjang.pack(side='left')
        self.frame_header.place(x=0,y=0)

        #headerrr aplikasi1
        self.nama_aplikasi = tkinter.Label(self.jendela,text='E-Kasir',fg='white',font='courier',bg='#282e28',width=55)
        self.nama_aplikasi.place(x=0,y=50)
        #body_aplikasi_
        self.body = tkinter.Canvas(self.jendela,bg='#282e28',width=546)
        self.body.place(x=0,y=125)

        #inputan_aplikasi():
        self.frame_inputan = tkinter.Frame(self.jendela)
        self.input_nama_barang = tkinter.Label(self.frame_inputan,text='Nama Barang',bg='#282e28',fg='white',font='courier',width=15)
        self.entry_nama_barang = tkinter.Entry(self.frame_inputan,width=35)
        self.input_nama_barang.pack(side='left')
        self.entry_nama_barang.pack(side='left')
        self.frame_inputan.place(x=5,y=150)


        self.frame_inputan1 = tkinter.Frame(self.jendela)
        self.input_harga = tkinter.Label(self.frame_inputan1,text='Harga Barang',bg='#282e28',fg='white',font='courier',width=15)
        self.entry_harga_in = tkinter.Entry(self.frame_inputan1,width=35)
        self.input_harga.pack(side='left')
        self.entry_harga_in.pack(side='left')
        self.frame_inputan1.place(x=5,y=190)


        self.frame_inputan2 = tkinter.Frame(self.jendela)
        self.input_jumlah = tkinter.Label(self.frame_inputan2,text='Jumlah Barang',bg='#282e28',fg='white',font='courier',width=15)
        self.entry_jumlah = tkinter.Entry(self.frame_inputan2,width=35)
        self.input_jumlah.pack(side='left')
        self.entry_jumlah.pack(side='left')
        self.frame_inputan2.place(x=5,y=230)


        self.frame_inputan3 = tkinter.Frame(self.jendela)
        self.input_jumlah_tunai = tkinter.Label(self.frame_inputan3,text='Jumlah Tunai',bg='#282e28',fg='white',font='courier',width=15)
        self.entry_jumlah_1 = tkinter.Entry(self.frame_inputan3,width=35)
        self.input_jumlah_tunai.pack(side='left')
        self.entry_jumlah_1.pack(side='left')
        self.frame_inputan3.place(x=5,y=275)




        self.cetak = tkinter.Button(self.jendela,text = 'Input',relief='flat',width=15,command=self.tombol_tambah)
        self.cetak.place(x=25,y=330)
        self.tambah = tkinter.Button(self.jendela,text = 'Cetak Total',relief='flat',width=15,command=self.cetak_total)
        self.tambah.place(x=150,y=330)
        self.delete = tkinter.Button(self.jendela,text='Delete Data',relief='flat',width=15,command=self.hapus)
        self.delete.place(x=275,y=330)




        self.footer = tkinter.Frame(self.jendela)
        self.text = tkinter.Label(self.footer,text='DEV | Mohamad Rizky Isa',width=100,bg='#282e28',fg='white',height=2)
        self.text.pack()
        self.footer.pack(side='bottom')
        self.jendela.mainloop()
    def tombol_tambah(self):
        harga_barang = int(self.entry_harga_in.get())
        jumlah_barang = int(self.entry_jumlah.get())
        taksiran = harga_barang*jumlah_barang
        data.append(taksiran)
    def hapus(self):
        data.clear()
    def cetak_total(self):
        tunai = int(self.entry_jumlah_1.get())
        c = sum(data)
        x = sum(data)-tunai
        tkinter.messagebox.showinfo('TOTAL','Total Kembalian : Rp {:,} \n Total Harga : {:,}'.format(x,c))
    def biodata(self):
        tkinter.messagebox.showinfo('About','APLIKASI INI DI BUAT UNTUK PEMBELAJARAN \n JIKA KALIAN INGIN MENGEMBANGKAN APLIKASI INI \n CONTACT : Instagram @kikiisa13 Wa 081245450978 Fb kikiisa')

    def log_out(self):
        def hancurkan():
            self.jendela.destroy()
        hancurkan()
    def pengaturan(self):
        class konfigurasi():
            def __init__(self):
                self.window = tkinter.Tk()
                self.window.geometry('300x300')
                self.window.config(bg='gray')

                self.label1 = tkinter.Frame(self.window,width=1000,height=22,bg='#282e28')
                self.label1.place(x=0,y=0)

                self.change = tkinter.Label(self.window,text='Change Id and Password',bg='#282e28',fg='white',font='arial 10 bold')
                self.change.place(x=0,y=0)

                self.frame1 = tkinter.Frame(self.window)
                self.label1 = tkinter.Label(self.frame1,text='Masukan Id Lama  ',bg='#282e28',fg='white')
                self.label2 = tkinter.Entry(self.frame1)
                self.label1.pack(side='left')
                self.label2.pack(side='left')
                self.frame1.place(x=20,y=50)

                self.frame2 = tkinter.Frame(self.window)
                self.label3 = tkinter.Label(self.frame2,text='Masukan Ps Baru  ',bg='#282e28',fg='white')
                self.label4 = tkinter.Entry(self.frame2)
                self.label3.pack(side='left')
                self.label4.pack(side='left')
                self.frame2.place(x=20,y=100)


                self.frame3 = tkinter.Button(self.window,text='Save',width=15,relief='flat',command=self.ganti_password)
                self.frame3.place(x=20,y=150)
                self.window.mainloop()
            def ganti_password(self):
                ambil_id_anda = str(self.label2.get())
                ambil_ps_baru = str(self.label4.get())
                x = sqlite3.connect('admin_login.db')
                v = x.cursor()
                v.execute('UPDATE login_admin SET pass = "%s" WHERE Usser = "%s" '%(ambil_ps_baru,ambil_id_anda))
                x.commit()
                def fungsi_hancurkan():
                    self.window.destroy()
                fungsi_hancurkan()
                tkinter.messagebox.showinfo('pemberitahuan','password anda berhasil di ubah')

        cek = konfigurasi()
run = aplikasi_pembelian()

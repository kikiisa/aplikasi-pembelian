import sqlite3
import tkinter.messagebox
class login():
    def __init__(self):
        self.jendela = tkinter.Tk()
        self.jendela.title('Login')
        self.jendela.geometry('400x400')
        self.jendela.config(bg='#282e28')


        self.canvas_bg = tkinter.Canvas(self.jendela,bg='#263126',)
        self.canvas_bg.place(x=9,y=50)

        self.judul = tkinter.Label(self.jendela,text='SIGN IN',font='arial 15 bold',fg='white',bg='#263126')
        self.judul.place(x=160,y=70)

        self.masuk = tkinter.Entry(self.jendela,width=30)
        self.masuk.insert(0,'Masukan Id')
        self.masuk.place(x=110,y=130)

        self.masuk1 = tkinter.Entry(self.jendela,width=30,show='*')
        self.masuk1.place(x=110,y=190)

        self.tombol = tkinter.Button(self.jendela,text='SIGN IN',font='courier 10 bold',relief='flat',width=22,bg='#00e66e',command=self.fungsi_admin)
        self.tombol.place(x=110,y=240)

        self.jendela.mainloop()
    def fungsi_admin(self):
        ambil_id = str(self.masuk.get())
        ambil_ps = str(self.masuk1.get())
        x = sqlite3.connect('admin_login.db')
        v = x.cursor()
        v.execute('SELECT * FROM login_admin')
        for baris in v:
            baris[0],baris[1]
        def seleksi():
            if ambil_id == baris[0] and ambil_ps == baris[1]:
                tkinter.messagebox.showinfo('Pemberitahuan','anda telah login')
                def hancurkan():
                    self.jendela.destroy()
                hancurkan()
                import interface      
            else:
                tkinter.messagebox.showerror('pemberitahuan','Galat')          
        seleksi()
        
run = login()

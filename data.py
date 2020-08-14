import sqlite3
nama = 'admin_login.db'
def main():
    x = sqlite3.connect(nama)
    v = x.cursor()
    #v.execute('CREATE TABLE login_admin (Usser CHAR,pass VARCHAR)')
    #v.execute('UPDATE login_admin SET Usser = "admin" WHERE pass = "kiki"')
    v.execute('SELECT * FROM login_admin')
    for baris in v:
        print(baris[0],baris[1])
    x.commit()
main()

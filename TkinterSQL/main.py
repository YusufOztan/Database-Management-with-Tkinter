import pyodbc
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calisan:
    def __init__(self,window):
        self.window = window
        self.window.title("Çalışan İşlemleri")
        self.frame = tk.Frame(self.window)
        self.frame.pack(side="left", fill="both", expand=True)

        self.label_id = tk.Label(self.frame, text="ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=0, column=1)

        self.label_ad = tk.Label(self.frame, text="Ad:")
        self.label_ad.grid(row=1, column=0)
        self.entry_ad = tk.Entry(self.frame)
        self.entry_ad.grid(row=1, column=1)

        self.label_soyad = tk.Label(self.frame, text="Soyad:")
        self.label_soyad.grid(row=2, column=0)
        self.entry_soyad = tk.Entry(self.frame)
        self.entry_soyad.grid(row=2, column=1)

        self.label_mail = tk.Label(self.frame, text="Çalışan Mail:")
        self.label_mail.grid(row=3, column=0)
        self.entry_mail = tk.Entry(self.frame)
        self.entry_mail.grid(row=3, column=1)

        self.label_tarih = tk.Label(self.frame, text="Çalışanın İşe Giriş Tarihi:(Y-A-G)")
        self.label_tarih.grid(row=4, column=0)
        self.entry_tarih = tk.Entry(self.frame)
        self.entry_tarih.grid(row=4, column=1)
        self.entry_tarih.bind("<KeyRelease>", self.validate_date)

        self.label_gorev = tk.Label(self.frame, text="Çalışanın Görevi:")
        self.label_gorev.grid(row=5, column=0)
        self.entry_gorev = tk.Entry(self.frame)
        self.entry_gorev.grid(row=5, column=1)

        self.label_maas = tk.Label(self.frame, text="Çalışanın Maaşı:")
        self.label_maas.grid(row=6, column=0)
        self.entry_maas = tk.Entry(self.frame)
        self.entry_maas.grid(row=6, column=1)

        self.label_yonetici_id = tk.Label(self.frame, text="Çalışanın bağlı olduğu yönetici:")
        self.label_yonetici_id.grid(row=7, column=0)
        self.entry_yonetici_id = tk.Entry(self.frame)
        self.entry_yonetici_id.grid(row=7, column=1)

        self.label_tckn = tk.Label(self.frame, text="Çalışanın TCKN:")
        self.label_tckn.grid(row=8, column=0)
        self.entry_tckn = tk.Entry(self.frame)
        self.entry_tckn.grid(row=8, column=1)

        self.label_telno = tk.Label(self.frame, text="Çalışan Telefon Numarası:")
        self.label_telno.grid(row=9, column=0)
        self.entry_telno = tk.Entry(self.frame)
        self.entry_telno.grid(row=9, column=1)

        self.button_ekle = tk.Button(self.frame, text="Veri Ekle", command=self.veri_ekle)
        self.button_ekle.grid(row=10, column=0, columnspan=2)

        self.label_id_2 = tk.Label(self.frame, text="Silinecek Çalışan ID'si:")
        self.label_id_2.grid(row=11, column=0)
        self.entry_id_2 = tk.Entry(self.frame)
        self.entry_id_2.grid(row=11, column=1)

        self.button_sil = tk.Button(self.frame, text="Veri Sil", command=self.veri_sil)
        self.button_sil.grid(row=12, column=0, columnspan=2)

        self.label_filtre_maas = tk.Label(self.frame, text="Maaş üzerinden filtreleme:")
        self.label_filtre_maas.grid(row=13, column=0)
        self.entry_filtre_maas = tk.Entry(self.frame)
        self.entry_filtre_maas.grid(row=13, column=1)

        self.button_filtrele = tk.Button(self.frame, text="Veri Filtrele", command=self.veri_filtrele)
        self.button_filtrele.grid(row=14, column=0, columnspan=2)

    def veri_ekle(self):
        calisan_id = self.entry_id.get()
        select_query = f"SELECT * FROM calisanlar WHERE calisanID = ?"
        c.execute(select_query, (calisan_id,))
        existing_employee = c.fetchone()

        if existing_employee:
            messagebox.showerror("Hata", "Bu ID'ye sahip bir çalışan zaten mevcut!")
        else:
            ad = self.entry_ad.get()
            soyad = self.entry_soyad.get()
            mail = self.entry_mail.get()
            tarih = self.entry_tarih.get()
            gorev = self.entry_gorev.get()
            maas = self.entry_maas.get()
            yonetici_id = self.entry_yonetici_id.get()
            TCKN = self.entry_tckn.get()
            telno = self.entry_telno.get()

            insert_query = f"INSERT INTO Calisanlar (calisanID, calisanAd, calisanSoyad, calisanEmail, iseGirisTarih, gorev, maas, yoneticiID, calisanTCKN, calisanTelNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(insert_query, (calisan_id, ad, soyad, mail, tarih, gorev, maas, yonetici_id, TCKN, telno))
            conn.commit()

            messagebox.showinfo("Bilgi", "Veri eklendi!")
            self.entry_id.delete(0, tk.END)
            self.entry_ad.delete(0, tk.END)
            self.entry_soyad.delete(0, tk.END)
            self.entry_mail.delete(0, tk.END)
            self.entry_tarih.delete(0, tk.END)
            self.entry_gorev.delete(0, tk.END)
            self.entry_maas.delete(0, tk.END)
            self.entry_yonetici_id.delete(0, tk.END)
            self.entry_tckn.delete(0, tk.END)
            self.entry_telno.delete(0, tk.END)

    def veri_sil(self):
        calisan_id = self.entry_id_2.get()

        delete_query = f"DELETE FROM calisanlar WHERE calisanID = {calisan_id}"
        c.execute(delete_query)
        conn.commit()

        messagebox.showinfo("Bilgi", "Veri silindi!")
        self.entry_id.delete(0, tk.END)

    def veri_filtrele(self):
        maas = self.entry_filtre_maas.get()

        select_query = f"SELECT calisanID, calisanAd, calisanSoyad, maas FROM calisanlar WHERE maas >= {maas}"
        c.execute(select_query)
        rows = c.fetchall()

        if not rows:
            messagebox.showinfo("Bilgi", "Veri bulunamadı!")
        else:
            table_window = tk.Toplevel()
            table_window.title("Filtrelenen Veriler")
            columns =["ID", "Ad", "Soyad", "Maaş"]
            tree = ttk.Treeview(table_window,columns=columns,show="headings")
            for col in columns:
                tree.column(col, width=300)
                tree.heading(col, text=col)
            for row in rows:
                tree.insert("", tk.END, values=tuple(row))

            tree.pack(fill='both', expand=True)

        self.entry_filtre_maas.delete(0, tk.END)

    def validate_date(self, event):
        date_string = self.entry_tarih.get()
        try:
            date = datetime.strptime(date_string,"%Y-%m-%d")
            self.entry_tarih.config(bg="green")
        except ValueError:
            self.entry_tarih.config(bg="red")

class StokDurumu:
    def __init__(self,window):
        self.window = window
        self.window.title("Stok Durumunu Düzenle / Kontrol Et")
        self.frame = tk.Frame(self.window)
        self.frame.pack(side="left", fill="both", expand=True)

        self.label_id = tk.Label(self.frame, text="Stok ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=0, column=1)

        self.label_urun_id = tk.Label(self.frame, text="Ürün ID:")
        self.label_urun_id.grid(row=1, column=0)
        self.entry_urun_id = tk.Entry(self.frame)
        self.entry_urun_id.grid(row=1, column=1)

        self.label_stok_adet = tk.Label(self.frame, text="Stok Adet:")
        self.label_stok_adet.grid(row=2, column=0)
        self.entry_stok_adet = tk.Entry(self.frame)
        self.entry_stok_adet.grid(row=2, column=1)

        self.label_fiyat = tk.Label(self.frame, text="Ürün Fiyat:")
        self.label_fiyat.grid(row=3, column=0)
        self.entry_fiyat = tk.Entry(self.frame)
        self.entry_fiyat.grid(row=3, column=1)

        self.label_tarih = tk.Label(self.frame, text="Son Güncellenme Tarihi:")
        self.label_tarih.grid(row=4, column=0)
        self.entry_tarih = tk.Entry(self.frame)
        self.entry_tarih.grid(row=4, column=1)
        self.entry_tarih.bind("<KeyRelease>", self.validate_date)

        self.label_adet = tk.Label(self.frame, text="Min Stok Adedi:")
        self.label_adet.grid(row=5, column=0)
        self.entry_adet = tk.Entry(self.frame)
        self.entry_adet.grid(row=5, column=1)

        self.label_a_tarihi = tk.Label(self.frame, text="Alım Tarihi:")
        self.label_a_tarihi.grid(row=6, column=0)
        self.entry_a_tarihi = tk.Entry(self.frame)
        self.entry_a_tarihi.grid(row=6, column=1)
        self.entry_a_tarihi.bind("<KeyRelease>", self.validate_date2)

        self.button_ekle = tk.Button(self.frame, text="Veri Ekle", command=self.veri_ekle)
        self.button_ekle.grid(row=7, column=0, columnspan=2)

        self.label_id_2 = tk.Label(self.frame, text="Silinecek Ürünün Stok ID'si:")
        self.label_id_2.grid(row=8, column=0)
        self.entry_id_2 = tk.Entry(self.frame)
        self.entry_id_2.grid(row=8, column=1)

        self.button_sil = tk.Button(self.frame, text="Veri Sil", command=self.veri_sil)
        self.button_sil.grid(row=9, column=0, columnspan=2)

        self.label_filtre_stok = tk.Label(self.frame, text="Stok Miktarı girilen miktardan az ise görüntüleme:")
        self.label_filtre_stok.grid(row=10, column=0)
        self.entry_filtre_stok= tk.Entry(self.frame)
        self.entry_filtre_stok.grid(row=10, column=1)

        self.button_filtrele = tk.Button(self.frame, text="Veri Filtrele", command=self.veri_filtrele)
        self.button_filtrele.grid(row=11, column=0, columnspan=2)

    def veri_ekle(self):
        stok_id = self.entry_id.get()
        urun = self.entry_urun_id.get()
        s_adet = self.entry_stok_adet.get()
        fiyat = self.entry_fiyat.get()
        tarih = self.entry_tarih.get()
        adet = self.entry_adet.get()
        a_tarihi = self.entry_a_tarihi.get()


        insert_query = f"INSERT INTO StokDurumu (stockID, urunID, stokAdet, urunFiyat, sonGuncellemeTarihi, minStokAdeti, alimTarihi) VALUES (?, ?, ?, ?, ?, ?, ?)"
        c.execute(insert_query, (stok_id, urun, s_adet, fiyat, tarih, adet, a_tarihi))
        conn.commit()


        messagebox.showinfo("Bilgi", "Veri eklendi!")
        self.entry_id.delete(0, tk.END)
        self.entry_urun_id.delete(0, tk.END)
        self.entry_stok_adet.delete(0, tk.END)
        self.entry_fiyat.delete(0, tk.END)
        self.entry_tarih.delete(0, tk.END)
        self.entry_adet.delete(0, tk.END)
        self.entry_a_tarihi.delete(0, tk.END)

    def veri_sil(self):
        stok_id = self.entry_id_2.get()

        delete_query = f"DELETE FROM StokDurumu WHERE stockID = {stok_id}"
        c.execute(delete_query)
        conn.commit()

        messagebox.showinfo("Bilgi", "Veri silindi!")
        self.entry_id.delete(0, tk.END)

    def veri_filtrele(self):
        stok_adet = self.entry_filtre_stok.get()

        select_query = f"SELECT *  FROM StokDurumu WHERE stokAdet <= {stok_adet}"
        c.execute(select_query)
        rows = c.fetchall()

        if not rows:
            messagebox.showinfo("Bilgi", "Veri bulunamadı!")
        else:
            table_window = tk.Toplevel()
            table_window.title("Filtrelenen Veriler")
            columns = ["Stok ID", "Ürün ID", "Stok Adet", "Ürün Fiyat", "Son Güncelleme Tarihi", "Min Stok Adedi", "Alım Tarihi"]
            tree = ttk.Treeview(table_window,columns=columns,show="headings")

            for col in columns:
                tree.column(col, width=100)
                tree.heading(col, text=col)

            for row in rows:
                tree.insert("", tk.END, values=tuple(row))

            tree.pack(fill='both', expand=True)

        self.entry_filtre_stok.delete(0, tk.END)

    def validate_date(self, event):
        date_string = self.entry_tarih.get()
        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")
            self.entry_tarih.config(bg="green")
        except ValueError:
            self.entry_tarih.config(bg="red")

    def validate_date2(self, event):
        date_string = self.entry_a_tarihi.get()
        try:
            date = datetime.strptime(date_string,  "%Y-%m-%d")
            self.entry_a_tarihi.config(bg="green")
        except ValueError:
            self.entry_a_tarihi.config(bg="red")

class UrunBilgi:
    def __init__(self,window):
        self.window = window
        self.window.title("Ürün Bilgisi Düzenle")
        self.frame = tk.Frame(self.window)
        self.frame.pack(side="left", fill="both", expand=True)

        self.label_id = tk.Label(self.frame, text="Ürün ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=0, column=1)

        self.label_urun_adi = tk.Label(self.frame, text="Ürün Adı:")
        self.label_urun_adi.grid(row=1, column=0)
        self.entry_urun_adi= tk.Entry(self.frame)
        self.entry_urun_adi.grid(row=1, column=1)

        self.label_kat = tk.Label(self.frame, text="Ürün Kategori")
        self.label_kat.grid(row=2, column=0)
        self.entry_kat = tk.Entry(self.frame)
        self.entry_kat.grid(row=2, column=1)

        self.label_fiyat = tk.Label(self.frame, text="Ürün Fiyat:")
        self.label_fiyat.grid(row=3, column=0)
        self.entry_fiyat = tk.Entry(self.frame)
        self.entry_fiyat.grid(row=3, column=1)

        self.label_T_ID = tk.Label(self.frame, text="Tedarikçi ID:")
        self.label_T_ID.grid(row=5, column=0)
        self.entry_T_ID = tk.Entry(self.frame)
        self.entry_T_ID.grid(row=5, column=1)

        self.button_ekle = tk.Button(self.frame, text="Veri Ekle", command=self.veri_ekle)
        self.button_ekle.grid(row=7, column=0, columnspan=2)

        self.label_id2 = tk.Label(self.frame, text="Silinecek Ürünün Ürün ID'si:")
        self.label_id2.grid(row=8, column=0)
        self.entry_id2 = tk.Entry(self.frame)
        self.entry_id2.grid(row=8, column=1)

        self.button_sil = tk.Button(self.frame, text="Veri Sil", command=self.veri_sil)
        self.button_sil.grid(row=9, column=0, columnspan=2)

        self.label_filtre_urun = tk.Label(self.frame, text="Ürün Kategorisi üzerinden görüntüleme:")
        self.label_filtre_urun.grid(row=10, column=0)
        self.entry_filtre_urun= tk.Entry(self.frame)
        self.entry_filtre_urun.grid(row=10, column=1)

        self.button_filtrele = tk.Button(self.frame, text="Veri Filtrele", command=self.veri_filtrele)
        self.button_filtrele.grid(row=11, column=0, columnspan=2)

        self.label_filtre_t_id = tk.Label(self.frame, text="Tedarikçi ID üzerinden görüntüleme:")
        self.label_filtre_t_id.grid(row=12, column=0)
        self.entry_filtre_t_id = tk.Entry(self.frame)
        self.entry_filtre_t_id.grid(row=12, column=1)

        self.button_filtrele2 = tk.Button(self.frame, text="Veri Filtrele", command=self.t_veri_filtrele)
        self.button_filtrele2.grid(row=13, column=0, columnspan=2)

    def veri_ekle(self):
        urun_id = self.entry_id.get()
        urun = self.entry_urun_adi.get()
        kategori = self.entry_kat.get()
        fiyat = self.entry_fiyat.get()
        t_id = self.entry_T_ID.get()


        insert_query = f"INSERT INTO UrunBilgi (urunID, urunAdi, urunKategori, urunFiyat, tedarikciID) VALUES (?, ?, ?, ?, ?)"
        c.execute(insert_query, (urun_id, urun, kategori, fiyat, t_id))
        conn.commit()


        messagebox.showinfo("Bilgi", "Veri eklendi!")
        self.entry_id.delete(0, tk.END)
        self.entry_urun_adi.delete(0, tk.END)
        self.entry_kat.delete(0, tk.END)
        self.entry_fiyat.delete(0, tk.END)
        self.entry_T_ID.delete(0, tk.END)


    def veri_sil(self):
        urunid = self.entry_id2.get()

        delete_query = f"DELETE FROM UrunBilgi WHERE urunID = {urunid}"
        c.execute(delete_query)
        conn.commit()

        messagebox.showinfo("Bilgi", "Veri silindi!")
        self.entry_id.delete(0, tk.END)

    def veri_filtrele(self):
        kat_filtre = self.entry_filtre_urun.get()

        select_query = f"SELECT *  FROM UrunBilgi WHERE LOWER(urunKategori) = LOWER('{kat_filtre}')"
        c.execute(select_query)
        rows = c.fetchall()

        if not rows:
            messagebox.showinfo("Bilgi", "Veri bulunamadı!")
        else:
            table_window = tk.Toplevel()
            table_window.title("Filtrelenen Veriler")
            columns = [ "Ürün ID", "Ürün Adı", "Ürün Kategori", "Ürün Fiyat", "Tedarikçi ID"]
            tree = ttk.Treeview(table_window,columns=columns,show="headings")

            for col in columns:
                tree.column(col, width=100)
                tree.heading(col, text=col)

            for row in rows:
                tree.insert("", tk.END, values=tuple(row))

            tree.pack(fill='both', expand=True)

        self.entry_filtre_urun.delete(0, tk.END)

    def t_veri_filtrele(self):
        t_filtre = self.entry_filtre_t_id.get()

        select_query = f"SELECT *  FROM UrunBilgi WHERE tedarikciID = {t_filtre}"
        c.execute(select_query)
        rows = c.fetchall()

        if not rows:
            messagebox.showinfo("Bilgi", "Veri bulunamadı!")
        else:
            table_window = tk.Toplevel()
            table_window.title("Filtrelenen Veriler")
            columns = ['Ürün ID', 'Ürün Adı', 'Ürün Kategori', 'Ürün Fiyat', 'Tedarikçi ID']
            tree = ttk.Treeview(table_window,columns=columns,show="headings")

            for col in columns:
                tree.column(col, width=100)
                tree.heading(col, text=col)

            for row in rows:
                tree.insert("", tk.END, values=tuple(row))

            tree.pack(fill='both', expand=True)

        self.entry_filtre_t_id.delete(0, tk.END)


class RaporuGoster:
    def __init__(self, window):
        self.window = window
        self.window.title("Raporlar")
        self.frame = tk.Frame(self.window)
        self.frame.pack(side="left", fill="both", expand=True)

        self.fig, self.axs = plt.subplots(figsize=(8, 6))
        self.axs.set_ylabel("Haftalık Toplam Satış Fiyatı")

        self.veri_gorsellestirme()

    def veri_gorsellestirme(self):
        select_query = "SELECT HaftalikToplamSatisFiyati, EnCokSatilanUrun FROM Raporlar"
        c.execute(select_query)
        rows = c.fetchall()

        satis_fiyatlari = [row[0] for row in rows]
        en_cok_satilan_urunler = [row[1] for row in rows]

        self.axs.clear()
        self.axs.bar(en_cok_satilan_urunler, satis_fiyatlari)
        self.axs.set_xlabel("En Çok Satılan Ürün")
        self.axs.set_ylabel("Haftalık Toplam Satış Fiyatı")
        self.axs.tick_params(axis='x', rotation=90)

        self.fig.tight_layout()

        if hasattr(self, "canvas"):
            self.canvas.draw()
        else:
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

        self.window.after(1000, self.veri_gorsellestirme)

class TablolariGoster:
    def __init__(self, window):
        self.window = window
        self.window.title("Market Verileri")
        self.window.geometry('300x300')
        self.tables = {
            "Calisanlar": "SELECT * FROM Calisanlar",
            "Musteriler": "SELECT * FROM Musteriler",
            "Raporlar": "SELECT * FROM Raporlar",
            "Satis": "SELECT * FROM Satis",
            "StokDurumu": "SELECT * FROM StokDurumu",
            "Tedarikciler": "SELECT * FROM Tedarikciler",
            "TedarikciUrun": "SELECT * FROM TedarikciUrun",
            "UrunBilgi": "SELECT * FROM UrunBilgi",
            "Yoneticiler": "SELECT * FROM Yoneticiler",
        }
        self.create_buttons()

    def create_buttons(self):
        for table_name, table_query in self.tables.items():
            button = tk.Button(self.window, text=table_name, command=lambda q=table_query: self.show_table(q))
            button.pack()

    def show_table(self, table_query):
        c.execute(table_query)
        rows = c.fetchall()
        table_window = tk.Toplevel(self.window)
        table_window.title("Tablo Verileri")
        table = ttk.Treeview(table_window)
        table.pack(fill='both', expand=True)

        columns = [column[0] for column in c.description]
        table["columns"] = columns

        for col in columns:
            table.column(col, width=100)
            table.heading(col, text=col)

        for row in rows:
            table.insert("", tk.END, values=tuple(row))


def tablolar():
    root = tk.Tk()
    tablo = TablolariGoster(root)
    root.mainloop()

def calisan_duzenle():
    root = tk.Tk()
    calisan = Calisan(root)
    root.mainloop()

def stok_duzenle():
    root = tk.Tk()
    stok = StokDurumu(root)
    root.mainloop()

def urun_duzenle():
    root = tk.Tk()
    stok = UrunBilgi(root)
    root.mainloop()

def verileri_gor():
    root = tk.Tk()
    stok = RaporuGoster(root)
    root.mainloop()

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-3O0Q4PH\SQLEXPRESS;'
    'Database=market;'
    'Trusted_Connection=True;'
)
c = conn.cursor()

window = tk.Tk()
window.title("Market VTYS")
window.geometry('800x400')

my_font = tkFont.Font(size= 14,weight="bold")
my_font2 = tkFont.Font(size= 11)

left_frame = tk.Frame(window,bg="#8B8B83")
left_frame.pack(side="left", fill="both", expand=True)

label_giris = tk.Label(left_frame, text="Market Veri Tabanı \n Yönetim Sistemine Hoşgeldiniz.\n"
                                    "Yapmak istediğiniz işlemi seçiniz.",font=my_font,bg="#8B8B83")
label_giris.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

right_frame = tk.Frame(window)
right_frame.pack(side="right", fill="both", expand=True)

islemler = tk.Label(right_frame, text="İşlemler",font=my_font)
islemler.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

button_tablo = tk.Button(right_frame, text="Verileri Görüntüle", command=tablolar,font=my_font2)
button_tablo.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

button_calisan = tk.Button(right_frame, text="Çalışan Bilgisi İşlemleri", command=calisan_duzenle,font=my_font2)
button_calisan.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

button_stok = tk.Button(right_frame, text="Stok Bilgisi İşlemleri", command=stok_duzenle,font=my_font2)
button_stok.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_urun = tk.Button(right_frame, text="Ürün Bilgisi İşlemleri", command=urun_duzenle,font=my_font2)
button_urun.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button_rapor = tk.Button(right_frame, text="Haftalık Toplam Satış Raporu Görüntüle", command=verileri_gor,font=my_font2)
button_rapor.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.mainloop()
# ==========================================
# SISTEM DATA TURNOVER KARYAWAN
# ==========================================

import datetime
from tabulate import tabulate

data_karyawan=[
    {"id":"K001","nama":"Andi Saputra","Jenis Kelamin":"Laki-laki","Usia":25,"Lama Bekerja":2,"Status Kerja":"Aktif","Alasan":"Masih Aktif"},
    {"id":"K002","nama":"Budi Santoso","Jenis Kelamin":"Laki-laki","Usia":29,"Lama Bekerja":5,"Status Kerja":"Resign","Alasan":"Gaji Kurang"},
    {"id":"K003","nama":"Citra Lestari","Jenis Kelamin":"Perempuan","Usia":28,"Lama Bekerja":3,"Status Kerja":"Resign","Alasan":"Karir Lebih Baik"},
    {"id":"K004","nama":"Dewi Anggraini","Jenis Kelamin":"Perempuan","Usia":27,"Lama Bekerja":6,"Status Kerja":"Resign","Alasan":"Lingkungan Kerja"},
    {"id":"K005","nama":"Eko Pratama","Jenis Kelamin":"Laki-laki","Usia":27,"Lama Bekerja":4,"Status Kerja":"Aktif","Alasan":"Masih Aktif"},
    {"id":"K006","nama":"Fitri Handayani","Jenis Kelamin":"Perempuan","Usia":29,"Lama Bekerja":3,"Status Kerja":"Resign","Alasan":"Pindah Kota"},
    {"id":"K007","nama":"Gilang Ramadhan","Jenis Kelamin":"Laki-laki","Usia":22,"Lama Bekerja":2,"Status Kerja":"Aktif","Alasan":"Masih Aktif"},
    {"id":"K008","nama":"Hani Putri","Jenis Kelamin":"Perempuan","Usia":26,"Lama Bekerja":2,"Status Kerja":"Aktif","Alasan":"Masih Aktif"},
    {"id":"K009","nama":"Indra Wijaya","Jenis Kelamin":"Laki-laki","Usia":28,"Lama Bekerja":5,"Status Kerja":"Resign","Alasan":"Karir Lebih Baik"},
    {"id":"K010","nama":"Jihan Aulia","Jenis Kelamin":"Perempuan","Usia":24,"Lama Bekerja":1,"Status Kerja":"Aktif","Alasan":"Masih Aktif"}
]

def tampilkan_tabel(data_karyawan):
    tabel=[]
    for k in data_karyawan:
        tabel.append([
            k["id"],
            k["nama"],
            k["Jenis Kelamin"],
            k["Lama Bekerja"],
            k["Status Kerja"],
            k["Alasan"]
        ])

    print(tabulate(tabel,
        headers=["id","nama","Jenis Kelamin","Lama Bekerja","Status Kerja","Alasan"],
        tablefmt='heavy_outline'))



#===MAIN MENU===
def tampilkan_main_menu():
    print("===== SISTEM DATA TURNOVER =====")
    print("1. Menu Read")
    print("2. Menu Create") 
    print("3. Menu Update")
    print("4. Menu Laporan & Analisis") 
    print("5. Menu Delete (Resign)")
    print("6. Keluar")

#===READ MENU===
def tampilkan_menu_read():

        print("\n===== SISTEM DATA KARYAWAN =====")
        print("1. Tampilkan Semua Data")
        print("2. Tampilkan Data Karyawan Berdasarkan ID Karyawan: ")
        print("3. Kembali ke Menu Utama")
        

def menu_read():
        while True:
            tampilkan_menu_read()
            pilihan = input("Pilih menu (1-3): ")

            if pilihan == "1":
                tampilkan_tabel(data_karyawan)
            elif pilihan == "2":
                cari_karyawan()
            elif pilihan == "3":
                break
            else:
                print("Pilihan tidak valid!")
                

#Tampilan Berdasarkan ID Karyawan
def cari_karyawan():
    while True:
        id_cari = input("Masukkan ID (contoh: K001): ").upper()

        if len(id_cari) == 4 and id_cari[0] == "K" and id_cari[1:].isdigit():
            break
        else:
            print("Format ID salah! Gunakan format seperti K001.")

    for k in data_karyawan:
        if k["id"] == id_cari:
            print("\nData Ditemukan:")
            for key, value in k.items():
                print(f"{key}: {value}")
            return

    print("Data tidak ditemukan.")


#===MENU CREATE===
def tampilkan_menu_create():
    print("\n===== MENU CREATE =====")
    print("1. Tambah Data Karyawan")
    print("2. Kembali")

#INPUT DATA
def menu_create():
    while True:
        tampilkan_menu_create()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tambah_karyawan_Baru()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

#Tambah Data Karyawan Baru
def tambah_karyawan_Baru():
    if len(data_karyawan) == 0:
        id_baru = "K001"
    else :
        id_baru = f"K{int(data_karyawan[-1]['id'][1:]) + 1:03d}"
#Validasi Nama
    while True:
        nama = input("Masukkan Nama (5-50 huruf): ").strip().title()

        if not nama:
            print("Nama tidak boleh kosong!")
        elif not all(c.isalpha() or c.isspace() for c in nama):
            print("Nama hanya boleh huruf!")
        elif len(nama) < 5:
            print("Nama minimal 5 karakter!")
        elif len(nama) > 50:
            print("Nama maksimal 50 karakter!")
        else:
            break
#Validasi Gender
    while True:
        jenis_kelamin = input("Jenis Kelamin (L/P): ").upper()
        if jenis_kelamin == "L":
            jenis_kelamin = "Laki-laki" 
            break
        elif jenis_kelamin == "P":
            jenis_kelamin = "Perempuan" 
            break
        else:
            print("Input salah! Masukkan hanya L atau P.")
#Validasi Usia
    tahun_sekarang = datetime.datetime.now().year
    while True:
        try:
            tahun_lahir = int(input("Tahun Lahir (contoh: 1997-2012): "))
            usia = tahun_sekarang - tahun_lahir
            if 18 <= usia <= 29:
                break
            else:
                print("Usia hanya boleh 18-29 tahun!")
        except ValueError:
            print("Usia harus berupa angka!")
#Validasi Lama Bekerja
    while True:
        try:
            tahun_masuk = int(input("Tahun Masuk Kerja: "))
            lama_bekerja = tahun_sekarang - tahun_masuk

            if tahun_masuk <= tahun_sekarang and lama_bekerja >= 0:
                if usia - lama_bekerja >= 17:
                    break
                else:
                    print("Tidak masuk akal, usia mulai kerja terlalu kecil!")
            else:
                print("Tahun masuk tidak valid!")
        except ValueError:
            print("Harus angka!")
#Validasi Status kerja
    while True:
        status = input("Status (Aktif/Resign): ").capitalize()
        if status in ["Aktif", "Resign"]:
            break
        else:
            print("Input hanya Aktif atau Resign!")
#Validasi Pilih Alasan Resign
    if status.lower() == "resign":
        print("Pilih Alasan Resign:")
        for i in range(len(daftar_alasan)):
            print(f"{i+1}. {daftar_alasan[i]}")

        while True:
            pilih = input("Masukkan pilihan: ")
            if pilih.isdigit() and 1 <= int(pilih) <= len(daftar_alasan):
                alasan = daftar_alasan[int(pilih)-1]
                break
            else:
                print("Pilihan tidak tersedia.")
    else:
        alasan = "Masih Aktif"
#Simpan Data Karyawan
    data_karyawan.append({
        "id": id_baru,
        "nama": nama,
        "Jenis Kelamin": jenis_kelamin,
        "Usia": usia,
        "Lama Bekerja": lama_bekerja,
        "Status Kerja": status,
        "Alasan": alasan
    })

    print("Data berhasil ditambahkan!")

#INPUT DATA
def menu_create():
    while True:
        tampilkan_menu_create()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tambah_karyawan_Baru()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

#===UPDATE MENU===
def tampilkan_menu_update():
    print("\n===== MENU UPDATE =====")
    print("1. Update Status Menjadi Resign")
    print("2. Kembali ke Menu Utama")

#UPDATE DATA
def menu_update():
    while True:
        tampilkan_menu_update()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tambah_data_resign()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")
   

#TAMBAH DATA KARYAWAN RESIGN
# ===LIST ALASAN RESIGN===
daftar_alasan = [
    "Gaji Kurang",
    "Lingkungan Kerja",
    "Pindah Kota",
    "Karir Lebih Baik"
]

def tambah_data_resign():
    while True:
        id_cari = input("Masukkan ID Karyawan (contoh: K001): ").upper()

        if len(id_cari) == 4 and id_cari[0] == "K" and id_cari[1:].isdigit():
            break
        else:
            print("Format ID salah! Gunakan format seperti K001.")

    ditemukan = False

    for k in data_karyawan:
        if k["id"] == id_cari:
            if k["Status Kerja"].lower() == "resign":
                print("Karyawan sudah berstatus resign.")
            else:
                print("\n=== Pilih Alasan Resign ===")
                for i, alasan in enumerate(daftar_alasan, start=1):
                    print(f"{i}. {alasan}")

                while True:
                    try:
                        pilihan = int(input("Pilih nomor alasan: "))
                        if 1 <= pilihan <= len(daftar_alasan):
                            k["Status Kerja"] = "Resign"
                            k["Alasan"] = daftar_alasan[pilihan - 1]
                            print("Status karyawan berhasil diubah menjadi resign.")
                            break
                        else:
                            print("Pilihan tidak tersedia.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

            ditemukan = True
            break

    if not ditemukan:
        print("ID karyawan tidak ditemukan.")

#INPUT DATA
def menu_update():
    while True:
        tampilkan_menu_update()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tambah_data_resign()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")


#===Menu Laporan & Analisis===
def tampilkan_menu_laporan():
    print("\n===== MENU LAPORAN & ANALISIS =====")
    print("1. Total Karyawan Resign")
    print("2. Hitung Turnover")
    print("3. Analisis Alasan Resign")
    print("4. Kembali")

#INPUT DATA
def menu_laporan():
    while True:
        tampilkan_menu_laporan()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tampilkan_karyawan_resign()
        elif  pilihan == "2":
            hitung_turnover()
        elif pilihan == "3":
            analisis_alasan_resign()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")

#TAMPILKAN KARYAWAN RESIGN
def tampilkan_karyawan_resign():
    print("\n===== DAFTAR KARYAWAN RESIGN =====")
    ada = False

    for k in data_karyawan:
        if k["Status Kerja"].lower() == "resign":
            print(f"{k['nama']} - {k['Alasan']}")
            ada = True

    if not ada:
        print("Tidak ada karyawan yang resign.\n")

#MENGHITUNG TURNOVER
def hitung_turnover():
    total = len(data_karyawan)
    resign = sum(1 for k in data_karyawan 
                 if k["Status Kerja"].lower() == "resign")
    
    if total == 0:
        print("Belum ada data.")
        return
    
    rate = (resign / total) * 100
    print("\n===== LAPORAN TURNOVER =====")
    print(f"Total Karyawan : {total}")
    print(f"Total Resign   : {resign}")
    print(f"Turnover Rate  : {rate:.2f}%")

#ANALISIS RESIGN
def analisis_alasan_resign():
    data_alasan = {}

    for k in data_karyawan:
        status= k.get("Status Kerja","").strip().lower()

        if status == "resign":
            alasan = k.get("Alasan", "Tidak diketahui")
            data_alasan[alasan] = data_alasan.get(alasan, 0) + 1

    if not data_alasan:
        print("\nBelum ada data resign.")
        return

    print("\n===== ANALISIS ALASAN RESIGN =====")
    for alasan, jumlah in data_alasan.items():
        print(f"{alasan} : {jumlah} orang")

    alasan_terbanyak = max(data_alasan, key=data_alasan.get)
    print("\nAlasan Resign Terbanyak:", alasan_terbanyak)


#===DELETE MENU===
def tampilkan_menu_delete():
    print("\n===== MENU DELETE =====")
    print("1. Hapus Data Karyawan")
    print("2. Kembali")

#INPUT DATA
def menu_delete():
    while True:
        tampilkan_menu_delete()
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            delete_karyawan_resign()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

#DELETE KARYAWAN YANG SUDAH RESIGN
def delete_karyawan_resign():
    id_cari = input("Masukkan ID: ").upper()
    ditemukan = False

    for k in data_karyawan:
        if k["id"] == id_cari:
            ditemukan = True

            if k["Status Kerja"].lower() == "resign":
                data_karyawan.remove(k)
                print("Data karyawan resign berhasil dihapus.")
            else:
                print("Karyawan masih aktif. Tidak bisa dihapus.")
            break
    if not ditemukan:
        print("ID tidak ditemukan.")


#MAIN MENU
def main_menu():
    while True:
        tampilkan_main_menu()
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            menu_read()
        elif pilihan == "2":
            menu_create()
        elif pilihan == "3":
            menu_update()
        elif pilihan == "4":
            menu_laporan()
        elif pilihan == "5":
            menu_delete()   
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

main_menu()


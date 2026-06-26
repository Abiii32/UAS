import csv
import os
from collections import deque

FILE_CSV = "buku.csv"

# Queue untuk antrian peminjaman
antrian_peminjaman = deque()

# Hash Map kategori buku
kategori_buku = {
    "Novel": [],
    "Pendidikan": [],
    "Teknologi": [],
    "Sejarah": []
}


# Membuat file CSV jika belum ada
def buat_file():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Judul", "Pengarang", "Tahun", "Stok", "Kategori"])


# Membaca data dari CSV
def baca_data():
    data = []
    with open(FILE_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# Menyimpan data ke CSV
def simpan_data(data):
    with open(FILE_CSV, mode="w", newline="") as file:
        fieldnames = ["ID", "Judul", "Pengarang", "Tahun", "Stok", "Kategori"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


# CREATE
def tambah_buku():
    print("\n=== Tambah Buku ===")

    id_buku = input("ID Buku : ")
    judul = input("Judul : ")
    pengarang = input("Pengarang : ")
    tahun = input("Tahun Terbit : ")
    stok = input("Stok : ")
    kategori = input("Kategori : ")

    data = baca_data()

    data.append({
        "ID": id_buku,
        "Judul": judul,
        "Pengarang": pengarang,
        "Tahun": tahun,
        "Stok": stok,
        "Kategori": kategori
    })

    simpan_data(data)
    print("Buku berhasil ditambahkan!")


# READ
def lihat_buku():
    print("\n=== Daftar Buku ===")

    data = baca_data()

    if not data:
        print("Data kosong.")
        return

    print("-" * 80)
    print(f"{'ID':<5}{'Judul':<25}{'Pengarang':<20}{'Stok':<10}")
    print("-" * 80)

    for buku in data:
        print(f"{buku['ID']:<5}{buku['Judul']:<25}{buku['Pengarang']:<20}{buku['Stok']:<10}")


# UPDATE
def update_buku():
    data = baca_data()

    id_buku = input("Masukkan ID Buku yang ingin diupdate: ")

    ditemukan = False

    for buku in data:
        if buku["ID"] == id_buku:
            buku["Judul"] = input("Judul Baru : ")
            buku["Pengarang"] = input("Pengarang Baru : ")
            buku["Tahun"] = input("Tahun Baru : ")
            buku["Stok"] = input("Stok Baru : ")
            buku["Kategori"] = input("Kategori Baru : ")

            ditemukan = True
            break

    if ditemukan:
        simpan_data(data)
        print("Data berhasil diperbarui.")
    else:
        print("ID tidak ditemukan.")


# DELETE
def hapus_buku():
    data = baca_data()

    id_buku = input("Masukkan ID Buku yang akan dihapus: ")

    data_baru = [buku for buku in data if buku["ID"] != id_buku]

    if len(data_baru) < len(data):
        simpan_data(data_baru)
        print("Data berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")


# SEARCHING (Linear Search)
def cari_buku():
    data = baca_data()

    kata_kunci = input("Masukkan Judul Buku: ").lower()

    ditemukan = False

    for buku in data:
        if kata_kunci in buku["Judul"].lower():
            print("\nBuku Ditemukan")
            print("ID :", buku["ID"])
            print("Judul :", buku["Judul"])
            print("Pengarang :", buku["Pengarang"])
            print("Tahun :", buku["Tahun"])
            print("Stok :", buku["Stok"])
            print("Kategori :", buku["Kategori"])
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan.")


# SORTING (Bubble Sort)
def urutkan_buku():
    data = baca_data()

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            if data[j]["Judul"].lower() > data[j + 1]["Judul"].lower():
                data[j], data[j + 1] = data[j + 1], data[j]

    print("\n=== Buku Setelah Diurutkan ===")

    for buku in data:
        print(buku["ID"], "-", buku["Judul"])


# QUEUE PEMINJAMAN
def pinjam_buku():
    nama = input("Nama Peminjam : ")
    judul = input("Judul Buku : ")

    antrian_peminjaman.append((nama, judul))

    print("Peminjaman masuk antrian.")


def kembalikan_buku():
    if len(antrian_peminjaman) == 0:
        print("Tidak ada antrian.")
        return

    data = antrian_peminjaman.popleft()

    print("Pengembalian Diproses")
    print("Nama :", data[0])
    print("Buku :", data[1])


def lihat_antrian():
    print("\n=== Antrian Peminjaman ===")

    if len(antrian_peminjaman) == 0:
        print("Antrian kosong.")
        return

    nomor = 1

    for item in antrian_peminjaman:
        print(f"{nomor}. {item[0]} meminjam {item[1]}")
        nomor += 1


# MENU
def menu():
    buat_file()

    while True:
        print("\n")
        print("=" * 40)
        print(" SISTEM MANAJEMEN PERPUSTAKAAN ")
        print("=" * 40)
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Cari Buku")
        print("6. Urutkan Buku")
        print("7. Pinjam Buku")
        print("8. Kembalikan Buku")
        print("9. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih Menu : ")

        if pilihan == "1":
            tambah_buku()

        elif pilihan == "2":
            lihat_buku()

        elif pilihan == "3":
            update_buku()

        elif pilihan == "4":
            hapus_buku()

        elif pilihan == "5":
            cari_buku()

        elif pilihan == "6":
            urutkan_buku()

        elif pilihan == "7":
            pinjam_buku()

        elif pilihan == "8":
            kembalikan_buku()

        elif pilihan == "9":
            lihat_antrian()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


menu()
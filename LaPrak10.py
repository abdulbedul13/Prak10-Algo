# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:39:08 2021

@author: Abdullah
"""

list_nama = []
list_nilai = []


def pilihan1():
    print("[1. INPUT DATA]")
    list_prak = []
    list_nama.append(input("Masukkan nama mahasiswa: "))

    for i in range(3):
        list_prak.append(int(input("Masukkan nilai praktikum {}: ".format(i + 1))))

    list_nilai.append(list_prak)
    print("")


def pilihan2():
    print("[2. VIEW DATA]")
    print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3")
    print("--------------------------------")
    for nama, nilai in zip(list_nama, list_nilai):
        prak1, prak2, prak3 = nilai
        print("{} \t {} \t {} \t {}".format(nama, prak1, prak2, prak3))
    print("")


def pilihan3():
    print("[3. HITUNG RATA-RATA PRAK TIAP MAHASISWA]")
    nm = len(list_nilai)
    temp_rerata = [0] * nm
    for i in range(nm):
        nilai = list_nilai[i]
        hasil = 0
        np = len(nilai)
        for j in range(np):
            hasil += nilai[j]
        temp_rerata[i] = hasil / np

    for nama, rata2 in zip(list_nama, temp_rerata):
        print("{} = {}".format(nama, rata2))
    print("")


def pilihan4():
    print("[4. HITUNG RATA-RATA TIAP PRAK]")
    nm = len(list_nilai)
    list_prak = [0, 0, 0]

    for i in range(nm):
        nilai = list_nilai[i]
        np = len(nilai)
        for j in range(np):
            if j == 0:
                list_prak[0] += nilai[j]
            elif j == 1:
                list_prak[1] += nilai[j]
            else:
                list_prak[2] += nilai[j]

    for i in range(len(list_prak)):
        print("Rerata Prak {}=".format(i + 1), list_prak[i] / nm)
    print("")


def pilihan5():
    print("[5. MENCARI NILAI RATA-RATA PRAK TIAP MAHASISWA]")
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    if nama in list_nama:
        indeks = list_nama.index(nama)
        print("Rerata nilai praktikum {} =".format(nama), sum(list_nilai[indeks]) / len(list_nilai[indeks]), "\n")


def pilihan6():
    print("[6. UPDATE NILAI PRAK MAHASISWA]")
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    if nama in list_nama:
        indeks = list_nama.index(nama)
        prak_ke = int(input("Ingin update nilai praktikum ke-: "))
        if 0 < prak_ke < 4:
            nilai_baru = int(input("Nilai baru: "))
            list_nilai[indeks][prak_ke - 1] = nilai_baru
            print("")


def mulai():
    while True:
        print("PROGRAM LIST")
        print("1. Input Data")
        print("2. View Data")
        print("3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa")
        print("4. Hitung Nilai Rata-Rata Tiap Praktikum")
        print("5. Mencari Nilai Rata-Rata Praktikum Mahasiswa")
        print("6. Update Nilai Praktikum Mahasiswa")
        print("7. Exit")
        pilihan = input("Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            pilihan1()

        elif pilihan == "2":
            pilihan2()

        elif pilihan == "3":
            pilihan3()

        elif pilihan == "4":
            pilihan4()

        elif pilihan == "5":
            pilihan5()

        elif pilihan == "6":
            pilihan6()

        elif pilihan == "7":
            print("[7. EXIT]")
            print("TERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, 3, 4, 5, 6 atau 7 untuk keluar\n")


if __name__ == "__main__":
    mulai()

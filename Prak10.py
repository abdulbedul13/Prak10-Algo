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

        elif pilihan == "7":
            print("[7. EXIT]\nTERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, 3 atau 7 untuk keluar\n")


if __name__ == "__main__":
    mulai()

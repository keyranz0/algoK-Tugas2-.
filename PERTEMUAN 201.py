"""
Aplikasi Hitung Luas Segitiga
Input: nilai Alas dan Tinggi
Output: nilai Luas Segitiga
dibuat oleh: Keyran
Tanggal Buat: 2024-11-28
"""

#membuat salam pembuka
print("Aplikasi Hitung Luas Segitiga")

#input Nilai Alas
alas = input("Nilai Alas: ")

#input Nilai Tinggi
tinggi = input("Nilai Tinggi: ")

#proses
luas = float(alas)* float(tinggi) *0.5
txluas = "Luasnya: " + str(luas)

#output 
print(txluas)

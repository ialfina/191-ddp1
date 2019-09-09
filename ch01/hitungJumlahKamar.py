'''

Mahasiswa Fasilkom Angkatan 2019 sedang merencanakan acara jalan-jalan. 
Bantulah ketua angkatan untuk menentukan jumlah kamar yang perlu disewa 
dan total biaya penginapan yang perlu dikeluarkan.

Input: jumlah mahasiswa pria, jumlah mahasiswa wanita, jumlah hari menginap

Output: cetak jumlah kamar yang harus disewa, berikut jumlah biaya menginap

Constraint:
Asumsikan hanya ada satu harga kamar, yaitu Rp.300.000/malam
Satu kamar hanya bisa diisi oleh mahasiswa dengan dengan gender yang sama
Satu kamar maksimal diisi oleh 3 mahasiswa

'''

import math

jum_pria = int(input("Masukkan jumlah mahasiswa pria: "))
jum_wanita = int(input("Masukkan jumlah mahasiswa wanita: "))
jum_hari = int(input("Masukkan jumlah hari: "))

jumlah_kamar_pria = math.ceil(jum_pria/3)
jumlah_kamar_wanita = math.ceil(jum_wanita/3)
jumlah_kamar_total = jumlah_kamar_pria + jumlah_kamar_wanita

harga_total = jumlah_kamar_total * jum_hari * 300000

print("Jumlah kamar total: ", jumlah_kamar_total)
print("Biaya total: Rp.", harga_total)

'''
Soal:

Sebuah sekolah sedang merencanakan acara jalan-jalan. Mereka perlu menyewa bus untuk mengangkut para siswa dan guru. 
Bantulah sekolah ini untuk menentukan jumlah bus yang perlu disewa berikut total biaya sewanya.
Input program: jumlah siswa dan jumlah guru
Output: Cetak jumlah bus yang perlu disewa dan total biaya sewanya.
Constraint: 
Satu bus bisa memuat 30 orang penumpang
Setiap siswa mendapatkan satu tempat duduk
Setiap guru mendapatkan dua tempat duduk, karena akan membawa perlengkapan acara
Untuk konsumsi dibutuhkan tambahan tempat duduk, dimana satu tempat duduk maksimal bisa digunakan untuk meletakkan 
kotak konsumsi untuk 10 orang peserta
Harga sewa harian per bus adalah 2 juta rupiah

'''

import math

jumlah_siswa = int(input("Masukkan jumlah siswa: "))
jumlah_guru = int(input("Masukkan jumlah guru: "))

jumlah_kursi_siswa = jumlah_siswa
jumlah_kursi_guru = jumlah_guru * 2
jumlah_kursi_konsumsi = math.ceil((jumlah_siswa + jumlah_guru)/10)

jumlah_kursi_total = jumlah_kursi_siswa + jumlah_kursi_guru + jumlah_kursi_konsumsi

jumlah_bus = math.ceil(jumlah_kursi_total/30)
total_biaya = jumlah_bus * 2000000

print("Jumlah bus: ", jumlah_bus)
print("Total biaya: ", total_biaya)


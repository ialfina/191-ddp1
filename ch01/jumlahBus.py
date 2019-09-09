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


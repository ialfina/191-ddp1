import csv

class Mahasiswa(object):

	def __init__(self, npm="", nama="", kelas="B"):
		self.npm = npm
		self.nama = nama
		self.kelas = kelas

	def __str__(self):
		strMhs = "NPM: " + self.npm + ", Nama: " + self.nama + ", Kelas: " + self.kelas

		return strMhs


class MahasiswaDB(object):

	def __init__(self, daftar = {}):
		self.daftar = daftar

	def importFromCSV(self, fileName):
		
		with open(fileName) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for line in csv_reader:
				aMhs = Mahasiswa(line[0], line[1], line[2])
				self.daftar[line[0]] = aMhs

		return len(self.daftar)


	def cariByNama(self, aName):
		
		result = []
		for v in self.daftar.values():
			if aName.lower() in v.nama.lower():
				result.append(v)

		return result

###########################################
# TESTING the Model
###########################################
def main():

	ddp1 = MahasiswaDB()
	n_data = ddp1.importFromCSV("ddp1_daftar_mhs.csv")
	if n_data>0:
		print("Sudah tersalin {} data".format(n_data))

	result = ddp1.cariByNama("san")

	print(len(result))

	for item in result:
		print(item)


if __name__ == "__main__":
	main()


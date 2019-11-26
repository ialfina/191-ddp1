"""
The Model component of BudayaKB app.
Contains two classes:
- class BudayaItem : the representation of a data in BudayaKB app
- class BudayaCollection: the representation of the collection of BudataItem objects

Author: Ika Alfina (ika.alfina@cs.ui.ac.id)

Last update: 26 November 2019
"""
import csv

"""
class BudayaItem
This class represents a data in BudayaKB app.
The data contains 4 field:
- nama (unique)
- tipe (the type of the data)
- prov (the province)
- URL

"""
class BudayaItem(object):

	def __init__(self, nama = "", tipe = "", prov = "", url = ""):
		"""
		The constructor of BudayaItem
		"""
		self.nama = nama
		self.tipe = tipe
		self.prov = prov
		self.url = url

	def __str__(self):
		"""
		Return a string that deescribes an instance of BudayaItem
		"""
		return self.nama + ", " + self.tipe + ", " + self.prov + ", " + self.url

	def __lt__(self, anotherBudayaItem):
		"""
		Override "less than" operation, so that this object can be sorted by "nama" field
		"""
		return self.nama < anotherBudayaItem.nama

	def __eq__(self, anotherBudayaItem):
		"""
		Override "equal" operation, so that this object can be sorted by "nama" field
		"""
		return self.nama == anotherBudayaItem.nama

"""
class BudayaCollection
This class represents the data structure that stores the BudayaKB data
List of operations:
- import and export from a CSV file
- search by "nama", "tipe", and "prov"
- add, update and delete 
- statistics (data size, data size by tipe and by prov)

"""
class BudayaCollection(object):

	def __init__(self, koleksi = {}):
		"""
		The constructor of BudayaCollection object
		"""
		self.koleksi = koleksi

	def __str__(self):
		"""
		Return a string that describe the BudayaCollection object
		"""
		return str(self.koleksi)

	def importFromCSV(self, fileName):
		"""
		to import data from a CSV file, and create the BudayaCollection object
		return the number of data imported
		"""
		with open(fileName) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for line in csv_reader:
				if len(line) == 4 and line[0] != "":
					budItem = BudayaItem(line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip())
					if line[0] not in self.koleksi:
						self.koleksi[line[0]] = budItem

	def exportToCSV(self, fileName):
		"""
		to export the data from a BudayaCollection object to a CSV file
		return None
		"""
		fh = open(fileName, "w")
		resultStr = ""

		for value in self.koleksi.values():
			resultStr += str(value) + "\n"

		print(resultStr, file=fh)
		fh.close()

	def cariByNama(self, aName):
		"""
		Return a list contains BudayaItem object of a certain name

		"""
		result = []

		for item in self.koleksi:
			if aName.strip().lower() in item.lower():
				result.append(self.koleksi[item])

		return result

	def cariByTipe(self, aType):
		"""
		Return a list contains BudayaItem object of a certain type
		"""
		result = []

		for item in self.koleksi.values():
			if aType.strip().lower() in item.tipe.lower():
				result.append(item)

		return result

	def cariByProv(self, aProv):
		"""
		Return a list contains BudayaItem object of a certain prov
		"""
		result = []

		for item in self.koleksi.values():
			if aProv.strip().lower() in item.prov.lower():
				result.append(item)

		return result



	def tambah(self, aName, aTipe, aProv, anURL):
		"""
		To add a new data to a collection of BudayaItem
		return 1 if the new data has a new unique name and the addition has been done
		return 0 otherwise, new data is not processed
		"""

		if aName not in self.koleksi:
			newBudayaItem = BudayaItem(aName.strip(), aTipe.strip(), aProv.strip(), anURL.strip())
			self.koleksi[aName] = newBudayaItem
			return 1
		else:
			return 0



	def hapus(self, aName):
		"""
		To remove a data to the collection of BudayaItem
		return 1 if the removal has been done
		return 0 if the data does not exist
		"""

		if aName in self.koleksi:
			self.koleksi.pop(aName.strip())
			return 1
		else:
			return 0


	def ubah(self, aName, aTipe, aProv, anURL):
		"""
		To update a data in the collection of BudayaItem
		return 1 if the data tobe updated is in the collection and the update has been done
		return 0 if the old data with the same key (name) does not exist
		"""
		if aName in self.koleksi:
			newBudayaItem = BudayaItem(aName.strip(), aTipe.strip(), aProv.strip(), anURL.strip())
			self.koleksi[aName] = newBudayaItem
			return 1

		else:
			return 0

	def stat(self):
		"""
		Return the number of item in the collection
		"""
		return len(self.koleksi)

	def statByTipe(self):
		"""
		Return a dictionary contains the number of occurences of each type
		"""

		result = {}

		for v in self.koleksi.values():
			if v.tipe not in result:
				result[v.tipe] = 1
			else:
				result[v.tipe] +=1

		return result

	def statByProv(self):
		"""
		Return a dictionary contains the number of occurences of each prov
		"""
		result = {}
		for v in self.koleksi.values():
			if v.prov not in result:
				result[v.prov] = 1
			else:
				result[v.prov] +=1

		return result

	def __str__(self):
		"""
		Return a string that describe the object
		"""
		resultStr = ""

		for value in self.koleksi.values():
			resultStr += str(value) + "\n"

		return resultStr


#####################################################################################
# for testing 
#####################################################################################
def main():

	mydb = BudayaCollection()

	#### Test import
	print("=================================================")
	print("Test Import Data")
	mydb.importFromCSV("dataSmall.csv")
	print("ImporCSV: Sukses menambahkan {} data baru\n".format(len(mydb.koleksi)))
	print(mydb)
	
	#### Test cari
	print("=================================================")
	print("Test Cari Data")
	
	keyCari = "a"
	result = mydb.cariByNama(keyCari)
	result.sort()
	if len(result) > 0:
		print("CariByNama: Ditemukan {} data dengan nama {}".format(len(result), keyCari))
		for item in result:
			print(item)
		print()
	else:
		print("CariByNama: Tidak ada data dengan nama {}\n".format(keyCari))


if __name__ == "__main__":
	main()
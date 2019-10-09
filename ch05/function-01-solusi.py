#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Oct 9 2019
# @author: Ika Alfina (ika.alfina@cs.ui.ac.id)


'''
LATIHAN CHAPTER 5 - SOAL 1 (SOLUSI)

Ubahlah program ini agar bersifat modular dengan memindahkan beberapa bagian program 
menjadi fungsi-fungsi.
Buat juga fungsi main.

'''


#################################################################################
# Fungsi isAdaInputBukanInteger
#################################################################################

def isAdaInputBukanInteger(dataList):
	'''
	Memeriksa apakah sebuah list mengandung item yang bukan bilangan bulat
	'''

	result = False
	for data in dataList:

		if data.isdigit():
			pass					
		else: # ada data bukan digit
			result = True
			break

	return result

#################################################################################
# Fungsi isAdaInputBukanTahunValid
#################################################################################

def isAdaInputBukanTahunValid(dataList):
	'''
	Memeriksa apakah isi sebuah list merupakan digit dengan panjang 4 sesuai 
	format tahun YYYY
	'''

	result = False
	for data in dataList:
		if len(data) != 4:
			result = True
			break

	return result

#################################################################################
# Fungsi terimaInput
#################################################################################

def terimaInput():
	'''
	Meminta user memasukkan beberapa angka tahun dan menyimpannya dalam sebuah list.
	Minta user mengulang memasukkan sampai isiannya benar
	'''

	dataList = []
	isInputValid = False

	while(isInputValid == False):

		petunjukInputStr = '''
Masukkan beberapa angka tahun (minimal 2), gunakan spasi sebagai delimiter.
Contoh: 1990 1800 2000
	'''
		inputUser = input(petunjukInputStr)
		dataList = inputUser.split()

		# periksa jumlah data
		if len(dataList) < 2:
			print("Jumlah data yang Anda masukkan kurang dari 2 buah")
		else:
			#periksa apakah semua data merupakan bilangan bulat
			if isAdaInputBukanInteger(dataList):
				print("Data harus berupa bilangan bulat")
			else:

				# cek apakah string merupakan angka tahun yang valid (terdiri dari 4 digit)
				if isAdaInputBukanTahunValid(dataList):
					print("Input salah, angka tahun harus terdiri dari 4 digit")

				else:
					isInputValid = True

	return dataList

#################################################################################
# Fungsi konversiKeInt
#################################################################################

def konversiKeInt(aList):
	'''
	Mengubah sebuah list yang berisi string of integer menjadi integer
	'''

	# konversi isi list dari string ke integer
	for i in range(len(aList)):
		aList[i] = int(aList[i])

#################################################################################
# Fungsi isKabisat
#################################################################################

def isKabisat(tahun):
	'''
	Memeriksa apakah sebuah tahun merupakan tahun kabisat
	'''

	isKabisat = False
	if tahun % 4 == 0:
		if tahun % 100 != 0:
			isKabisat = True
		else:
			if tahun % 400 == 0:
				isKabisat = True

	return isKabisat

#################################################################################
# Fungsi main
#################################################################################

def main():

	dataList = terimaInput()
	konversiKeInt(dataList)

	for data in dataList:	
		if isKabisat(data):
			print(data, "adalah tahun kabisat")
		else:
			print(data, "BUKAN tahun kabisat")


#################################################################################
# Execute main
#################################################################################

if __name__ == '__main__':

	main()


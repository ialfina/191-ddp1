#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Oct 8 2019
# @author: Ika Alfina (ika.alfina@cs.ui.ac.id)


'''
LATIHAN CHAPTER 5 - SOAL 1

Ubahlah program ini agar bersifat modular dengan memindahkan beberapa bagian program 
menjadi fungsi-fungsi.
Buat juga fungsi main.

'''

# Meminta user memasukkan beberapa angka tahun dan menyimpannya dalam sebuah list.
# Minta user mengulang memasukkan sampai isiannya benar

dataList = []

isInputValid = False

while(isInputValid == False):

	petunjukInputStr = '''
Masukkan beberapa angka tahun (minimal 2), gunakan spasi sebagai delimiter.
Contoh: 1990 1800 2000
'''

	# print("Masukkan beberapa bilangan bulat (lebih dari 1), batasi dengan spasi:\n)
	inputUser = input(petunjukInputStr)

	'''
	cek apakah input benar berisi hanya bilangan bulat
	'''

	dataList = inputUser.split()

	# periksa jumlah data
	if len(dataList) < 2:
		print("Jumlah data yang Anda masukkan kurang dari 2 buah")
	else:
		#periksa apakah semua data merupakan bilangan bulat
		isAdaInputBukanInteger = False
		for data in dataList:

			if data.isdigit():
				pass					
			else: # ada data bukan digit
				isAdaInputBukanInteger = True
				break

		if isAdaInputBukanInteger:
			print("Data harus berupa bilangan bulat")
		else:

			# cek apakah string merupakan angka tahun yang valid (terdiri dari 4 digit)
			isAdaInputBukanTahunValid = False
			for data in dataList:
				if len(data) != 4:
					isAdaInputBukanTahunValid = True
					break

			if isAdaInputBukanTahunValid:
				print("Input salah, angka tahun harus terdiri dari 4 digit")

			else:
				isInputValid = True


# konversi isi list dari string ke integer
for i in range(len(dataList)):
	dataList[i] = int(dataList[i])


# cek untuk setiap input data apakah input tersebut merupakan tahun kabisat
for data in dataList:

	isKabisat = False
	if data % 4 == 0:
		if data % 100 != 0:
			isKabisat = True
		else:
			if data % 400 == 0:
				isKabisat = True

	if isKabisat:
		print(data, "adalah tahun kabisat")
	else:
		print(data, "BUKAN tahun kabisat")


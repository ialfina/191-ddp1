#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Oct 8 2019
# @author: Ika Alfina (ika.alfina@cs.ui.ac.id)


'''
LATIHAN CHAPTER 5 - SOAL 2

Ubahlah program ini, dengan mengubah fungsi isGenapReturnInt dan isGenapReturnBoolean
agar memiliki hanya satu statement return
'''

####################################################################################

def isGenapReturnInt(bilangan):
	'''
	Fungsi memeriksa apakah sebuah bilangan meerupakan bilangan genap atau bukan
	Input: sebuah bilangan 
	Return:
	- 1, jika input merupakan bilangan genap
	- 0 ,jika ganjil
	'''

	if bilangan%2 == 0:
		return 1
	else:
		return 0

####################################################################################

def isGenapReturnBoolean(bilangan):
	'''
	Fungsi memeriksa apakah sebuah bilangan meerupakan bilangan genap atau bukan
	Input: sebuah bilangan 
	Return:
	- True, jika input merupakan bilangan genap 
	- False, jika ganjil
	'''
	if bilangan%2 == 0:
		return True
	else:
		return False

####################################################################################

def main():

	# Test the functions

	bilangan = [1, 2, 3, 4]
	for bil in bilangan:
		if isGenapReturnInt(bil):
			print(bil, "adalah bilangan genap")
		else:
			print(bil, "adalah bilangan GANJIL")

	bilangan = [10, 33, 43, 3000]
	for bil in bilangan:
		if isGenapReturnBoolean(bil):
			print(bil, "adalah bilangan genap")
		else:
			print(bil, "adalah bilangan GANJIL")

####################################################################################

if __name__ == "__main__":
	main()

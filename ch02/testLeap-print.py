'''

Uji Kabisat

- Jika sebuah tahun habis dibagi 4, uji tambahan persyaratan sebagai berikut:
   - Jika tahun tersebut tidak habis dibagi 100, maka tahun tersebut adalah tahun kabisat
   - Jika tahun tersebut habis dibagi 100, uji lagi:
       - Jika tahun tersebut habis dibagi 400, maka tahun tersebut adalah tahun kabisat
       - Jika tidak habis, maka bukan tahun kabisat
- Jika tidak habis dibagi 4, maka bukan tahun kabisat

Test case:
Tahun kabisat: 1988, 1996, 2000
Tahun bukan kabisat: 1700, 1800, 1999

@author ialfina
@last update: 11 Sept 2019

'''

year = int(input("Masukkan tahun dalam 4 digit : "))

if year % 4 == 0:
	# cek habis dibagi 100
	if year % 100 != 0:
		print("{} ADALAH tahun kabisat.".format(year))
	else:
		if year % 400 == 0:
			print("{} ADALAH tahun kabisat.".format(year))
		else:   
			print("{} BUKAN tahun kabisat.".format(year)) 
			
else:   
	print("{} BUKAN tahun kabisat.".format(year))

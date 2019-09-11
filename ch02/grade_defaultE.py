'''

Menentukan grade nilai dalam rentang 0 - 100

A: nilai >= 85
B: 70 <= nilai < 85
C: 55 <= nilai < 70
D: 45 <= nilai < 55
E: nilai < 45

@author ialfina
@last_update 11 Sept 2019

'''

nilai = float(input("Masukkan nilai dalam interval (0, 100): "))
grade = 'E' # initialisasi dengan nilai default 'E'

if nilai >= 85 :
	grade = 'A'
elif nilai >= 70 :
	grade = 'B'
elif nilai >= 55 :
	grade = 'C'
elif nilai >= 45 :
	grade = 'D'
# else : # tidak perlu
# 	grade = 'E'

print("Nilai {} setara dengan grade {}".format(nilai, grade))

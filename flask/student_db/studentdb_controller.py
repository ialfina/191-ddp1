#!/usr/bin/env python3
'''
The Controller component of StudentDB app

Contains the implementation of 2 features:
- import the data from CSV file
- search data by student name

Author: Ika Alfina (ika.alfina@cs.ui.ac.id)
Last update: 26 November 2019

'''

from flask import Flask, render_template, request
from studentdb_model import Mahasiswa, MahasiswaDB
app = Flask(__name__)
app.secret_key ="ika"

databaseName = "ddp1_daftar_mhs.csv"
dataMhs = MahasiswaDB()


#####################################################################################
# Index
#####################################################################################

@app.route('/')
def index():
	return render_template('index.html')

#####################################################################################
# Import Data From A CSV File
#####################################################################################

@app.route('/importData', methods=['GET', 'POST'])
def importData():
	if request.method == "GET":
		return render_template('importDataForm.html')
 
	elif request.method == "POST":
		
		f = request.files['file']
		global databaseName
		databaseName = f.filename
		dataMhs = MahasiswaDB()
		dataMhs.importFromCSV(f.filename)
		n_imported = len(dataMhs.daftar)
		return render_template("importDataForm.html", result=n_imported, fname=f.filename)
		
#####################################################################################
# Search Student Data by a keyword of name
#####################################################################################

@app.route('/cariData', methods=['GET', 'POST'])
def cariData():
	queryNama = ""
	if request.method == "GET":	
		if len(request.args) == 0:
				return render_template('cariDataForm.html')
		else:
			queryNama = request.args['nama']
	elif request.method == "POST":
		queryNama = request.form['nama']

	# process query
	if queryNama != "":
		# dataMhs = MahasiswaDB()
		# dataMhs.importFromCSV(databaseName)
		resultCari = dataMhs.cariByNama(queryNama)
		resultCari.sort()
		return render_template("cariDataForm.html", result=resultCari, nama=queryNama)

#####################################################################################
# Run the App
#####################################################################################
if __name__ == '__main__':
   app.run(debug = True)
   
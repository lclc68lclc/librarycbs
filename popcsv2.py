djangoproject_home="C:Users\Linac\Desktop\venv\librarycbs\libraryinv"
import sys,os
sys.path.append(djangoproject_home)


import csv

from django.utils import timezone

from libraryinv.forms import PublisherForm

def import_csv(filename):
	rows = open('C:Users\Linac\Desktop\test_db.csv')
	records_added = 0
	errors = []
	#Generate a dict per row, with the first CSV row being the keys.
	for row in csv.DictReader(rows, delimiter=","):
	
		#Bind the row data to the MyModelForm
		form = PublisherForm(row)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			records_added += 1
		else:
			errors.append(form.errors)
			
	return records_added, errors
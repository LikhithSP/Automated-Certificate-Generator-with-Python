import csv
from docxtpl import DocxTemplate
import os

# Configuration
template = DocxTemplate('certificate-template.docx')
filename = 'data.csv'
output = 'certifications'

# Ensure the output directory exists
if not os.path.exists(output):
    os.makedirs(output)

# Read all rows from the CSV file
getList = []

with open(filename, 'r') as data:
    reader = csv.reader(data, delimiter=',')
    next(reader)  # Skip the header row
    for line in reader:
        if line:  # Avoid processing empty lines
            getList.append(line)

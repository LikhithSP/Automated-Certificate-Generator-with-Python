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

# Function to create files .docx
def create_certification():
    for names in getList:
        # Ensure there are enough columns in the row
        if len(names) < 4:
            print(f"Skipping row due to insufficient columns: {names}")
            continue
        # Column's Name
        date = names[0]
        name = names[1]
        head_event = names[2]
        mentor = names[3]
        context = {
            'date': date,
            'name': name,
            'head_event': head_event,
            'mentor': mentor,
        }
        template.render(context)
        template.save(f"{output}/{name.replace(' ', '_')}.docx")

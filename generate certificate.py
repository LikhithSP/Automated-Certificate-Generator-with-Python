import csv
from docxtpl import DocxTemplate
import os

# Configuration
template = DocxTemplate('certificate-template.docx')
filename = 'data.csv'
output = 'certifications'

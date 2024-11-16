## 🎗️ Automated Certificate Generation Using Python

<div align="center">
<img src="https://github.com/LikhithSP/automated-certificate-python/blob/main/images/output.png">
</div>

<p align="center"><strong>This project is designed to simplify and automate the process of generating certificates in .docx format</strong></p>

## 🌟 Project Overview
This repository demonstrates how to use Python to create, customize, and convert certificates efficiently. It leverages powerful libraries like python-docx, pdf2image, and pypandoc to handle document creation and conversion seamlessly.

## 📋 Features
Automated Certificate Creation: Generate certificates in bulk from a CSV file containing recipient details.

Document Conversion: Convert .docx files to PDF and subsequently to image formats like .png or .jpg.

Customizable Templates: Use and modify .docx templates for certificate generation.

Directory Management: Handle input and output directories for easy file management.

## 🚀 Getting Started
To get started with this project, follow these steps:

Clone the Repository:

sh
git clone https://github.com/your-username/automated-certificate.git
cd automated-certificate
Install Dependencies: Install the required Python libraries:

sh
pip install python-docx pdf2image pypandoc
Install Pandoc: Download and install Pandoc from the Pandoc website.

Prepare Your Data: Ensure your data.csv file is in the correct format and place it in the project directory.

Run the Script: Execute the script to generate certificates and convert them to images:

sh
python main.py
## 📂 Directory Structure
automated-certificate/
├── certificates/          # Input directory containing .docx certificate templates
├── images/                # Output directory for generated image files
├── data.csv               # CSV file with recipient details
├── certificate-template.docx # Template for certificate generation
├── main.py                # Main script for automation
└── README.md              # Project documentation
## 🛠️ Technologies Used
Python: The core programming language used for scripting.

python-docx: For reading and writing .docx files.

pdf2image: For converting PDF files to image formats.

pypandoc: For converting .docx files to PDF.

## 🤝 Contributions
Contributions are welcome! If you have ideas for improving this project or adding new features, feel free to fork the repository and submit a pull request. Issues and suggestions can also be raised in the Issues section.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact
For any inquiries, please reach out via email@example.com.

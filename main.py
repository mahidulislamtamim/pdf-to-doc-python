# Import Converter
from pdf2docx import Converter
import os

# Set file path
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file = os.path.join(script_dir, "MahidulIslam.pdf")
output_file = os.path.join(script_dir, "MahidulIslam.docx")

if not os.path.exists(pdf_file):
    # print file not found message
    print(f"File not found: {pdf_file}")
elif os.path.exists(output_file):
    # print file exists message
    print(f"File already exists: {output_file}")
else:
    # Convert file
    converter = Converter(pdf_file=pdf_file)
    converter.convert(output_file)
    converter.close()
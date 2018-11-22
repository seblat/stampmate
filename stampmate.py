#! /usr/bin/python3

"""
Stamp a set of files with their number taken from their file name.
The numeration within the naming has to be continous.
Eg.:
25.pdf --> 25_num.pdf
26.pdf --> 26_num.pdf
27.pdf --> 27_num.pdf
requirements:
- PyMuPDF
usage:
python3 stampmate <first_file_number> <folder>
Eg.:
python3 stampmate.py 19 ./test-files
"""

import os
import sys

#Check requirements
try:
    import fitz
except ModuleNotFoundError:
    print("please run `pip install PyMuPDF`")
    sys.exit(1)

# Validate CLI Arguments
try:
    assert len(sys.argv) == 3  # filename and two args
    assert sys.argv[1].isdigit()  # first arg is number
    assert os.path.exists(sys.argv[2])  # file exists

except AssertionError:
    print('please pass the number and the file name')
    sys.exit(1)

# add text and write to <filename>_num.pdf
file_number = int(sys.argv[1])
folder = sys.argv[2]


while os.path.exists(f'{folder}/{file_number}.pdf'):
    text = "Rechnung Nr. {}".format(file_number)
    new_file_name = f'{file_number}_num.pdf'
    doc = fitz.open(f'{folder}/{file_number}.pdf')
    page = doc[0]
    page.insertText(fitz.Point(60, 60),
                    text,
                    fontsize=30,
                    color=(255/255, 128/255, 0/255))
    doc.save(f'{folder}/{new_file_name}')
    print("Document saved as", new_file_name)
    file_number += 1

else:
    if file_number == int(sys.argv[1]): #No file has been stamped
        print(f'file_number {file_number} was not found in {folder}')
    else:
        print(f'All files in {folder} from {sys.argv[1]} upwards haven been stamped.')

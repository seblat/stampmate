#! /usr/bin/python3

"""
requirements:
- PyMuPDF
usage:
python3 stampmate <number> <file_name>
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
    assert sys.argv[2].lower().endswith('.pdf')
except AssertionError:
    print('please pass the number and the file name')
    sys.exit(1)

# add text and write to <filename>_num.pdf
number = int(sys.argv[1])
text = "Rechnung Nr. {}".format(number)
file_name = sys.argv[2]
new_file_name = file_name[:-4]+"_num"+file_name[-4:]

doc = fitz.open(file_name)
page = doc[0]
page.insertText(fitz.Point(60, 60),
                text,
                fontsize=30,
                color=(255/255, 128/255, 0/255))
doc.save(new_file_name)
print("Document saved as", new_file_name)

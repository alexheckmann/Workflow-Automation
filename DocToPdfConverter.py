import sys
import os
from _ctypes import COMError

import comtypes.client


def doc_to_pdf(_in, _out):
    pdf_format = 17
    file_in = os.path.abspath(_in)
    file_out = os.path.abspath(_out)
    
    try:
        worddoc = comtypes.client.CreateObject('Word.Application')
        doc = worddoc.Documents.open(file_in)
        doc.SaveAs(file_out, FileFormat=pdf_format)
        doc.Close()
        worddoc.Quit()
    except COMError:
        print("Could not read file:" + str(file_in))
    

destination = sys.argv[1]
for file in os.listdir(destination):
    in_filename = destination + "\\" + file
    file_extension = os.path.splitext(in_filename)[-1].lower()

    if file_extension == ".docx":
        out_filename = destination + "\\" + str(file).rstrip(".docx") + ".pdf"
        doc_to_pdf(in_filename, out_filename)
    else:
        continue

import os
import sys
from _ctypes import COMError

import comtypes.client


def retry(max_attempts):
    def tryIt(func):
        def f():
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func()
                except:
                    attempts += 1
            if attempts == max_attempts:
                print("\nExceeded number of maximum attempts, exiting script")

        return f

    return tryIt


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


@retry(5)
def batch_conversion():
    try:
        destination = sys.argv[1]
    except IndexError:
        destination = input("Please enter the destination folder:\n")

    for file in os.listdir(destination):
        in_filename = destination + "\\" + file
        file_extension = os.path.splitext(in_filename)[-1].lower()
        out_filename = destination + "\\" + str(file).rstrip(".docx") + ".pdf"

        if ".docx" in file_extension:
            pdf_filename = str(file).rstrip(".docx") + ".pdf"
            pdf_exists = pdf_filename in os.listdir(destination)
            if pdf_exists:
                print("PDF version of \"" + str(file) + "\" already exists")
            else:
                doc_to_pdf(in_filename, out_filename)
                print("PDF version of \"" + str(file) + "\" created")
        else:
            continue


batch_conversion()

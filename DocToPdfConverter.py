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
        destination = input("Please enter an absolute path to your destination folder:\n")
    finally:
        while True:
            try:
                for file in os.listdir(destination):
                    in_filename = destination + "\\" + file
                    file_extension = os.path.splitext(in_filename)[-1].lower()

                    if ".doc" in file_extension:
                        out_filename = destination + "\\" + str(file).rstrip(".docx") + ".pdf"
                        doc_to_pdf(in_filename, out_filename)
                    else:
                        continue
                break

            except OSError:
                destination = input("Please enter a valid path:\n")


batch_conversion()

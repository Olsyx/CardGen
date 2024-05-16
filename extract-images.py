import sys
import os
from os import path
from glob import glob  

import subprocess

def main(directory):
    output_path = ""
    output_folder = "Images"

    #TODO: Arreglar que el output va directamente a Images y yo quiero que vaya a Images/Nombre del PDF coññño

    if ".pdf" in directory:
        output_path = os.path.dirname(directory) + "\\" + output_folder
        extract_pngs(directory, output_path)
    else:
        output_path = directory + "\\" + output_folder
        extract_pngs_from_pdfs(directory, output_path)

    remove_duplicated_imgs(output_path)

def extract_pngs_from_pdfs(directory, output_path):    
    pdfs = glob(path.join(directory,"*.pdf"))

    for file in pdfs:
        extract_pngs(file, output_path)

def extract_pngs(file_path, output_path):
    output_name = os.path.basename(file_path).split('/')[-1].rsplit( ".", 1 )[0]
    command = "pdfimages -png \"" + file_path + "\" \"" + output_path + "\\" + output_name + "\""
    
    print("EXTRACTING >>>>>>> " + output_name)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()    

def remove_duplicated_imgs(directory):
    command = "python remove-duplicates.py \"" + directory + "\""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()    


main(sys.argv[1])
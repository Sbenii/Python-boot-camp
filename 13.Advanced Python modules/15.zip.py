f=open('Fileone.txt','w+')
f.write("This is the first text!!")
f.close()

f=open('Filetwo.txt','w+')
f.write("This is the second text!!")
f.close()

import zipfile
comp_file=zipfile.ZipFile("Compressed_file.zip","w")
comp_file.write('Fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('Filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj=zipfile.ZipFile('Compressed_file.zip','r')
zip_obj.extractall('Extracted_content')

import os
print(os.getcwd())

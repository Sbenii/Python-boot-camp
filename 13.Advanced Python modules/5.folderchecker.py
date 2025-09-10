#Here we are going to pass through folder using the for loop and then print out the files or subfolders in those folders
import os
file_path='/Users/beni/Documents/Skills/QA/Sebron'
for folder,sub_folders,files in os.walk(file_path):
    print(f"Currently looking at {folder} ")
    print('\n')
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")
    print('\n')
    print("The files are: ")
    for file in files:
        print(f"File: {file}")
    print('\n')
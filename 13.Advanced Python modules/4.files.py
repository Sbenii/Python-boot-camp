t=open('Test.txt','w+')
t.write("This is a test string!!")
t.close()
import os
print(os.getcwd())#-->shows where you are working in
print(os.listdir())#-->list all things in a given directory
import shutil
shutil.move('Test.txt','/users/beni/documents/skills/Machine Learning/Python/Python boot camp/13.Advanced Python modules')
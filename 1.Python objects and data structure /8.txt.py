with open("myfile.txt", "w+") as f:
    f.write("Hello this is my first text file in python!!")
    f.write("\nMy name is Beni!!")
    f.write("\n----------------------")
    f.seek(0)  # go back to the beginning of the file
    myfile = f.read()
    print(myfile)
with open("myfile.txt","+a") as f:
    f.write("\nThis is the appending function!!")
    f.seek(0)  # go back to the beginning of the file
    myfile = f.read()
    print(myfile)
    

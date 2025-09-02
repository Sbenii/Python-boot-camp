with open("myfile.txt", "w+") as f:
    f.write("Hello this is my first text file in python!!")
    f.seek(0)  # go back to the beginning of the file
    myfile = f.read()
    print(myfile)

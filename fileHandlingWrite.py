"""This file write text in a file."""
try:
    # If file exist then it will erase all the existing data
    # If file does not exist then it will create a new file
    handle = open("exampleWrite.txt", 'w')
except:
    print("File does not exist")
handle.write("Awesome we wrote one file!!")
handle.close()

try:
    handle = open("exampleRead.txt")
except:
    print("File does not exist")
print(handle.read())
# Now the pointer is reached at the end of the file
print("********************")
# Use Seek function to move the pointer at a particular position in a file
handle.seek(0)  # Now the pointer is at first position so we can read file again
for line in handle:
    print(line.rstrip())
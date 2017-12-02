try:
    # If file exist then append text and if not exist then it will create  new file
    handle = open("exampleWrite2.txt", 'a')
except:
    print("File does not exist")
handle.write("\nAwesome we appended text to existing file!!")
import re

hand = ['From: ankit@gmail.com', 'To: ankit@gmail.com']
for line in hand:
    line = line.rstrip()
    print("re.search('From:', line):", re.search('From:', line), "\n")
    if re.search('From:', line):
        print(line)

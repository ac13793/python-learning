items = [1,2,3,4,5]
print("type(items):", type(items))

# Although a list can contain another list, the nested list still counts as a single
# element. The length of this list is four:
nestedlist = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print("len(nestedlist):", len(nestedlist))

#  Convert a string into a list
names = 'Ankit Shanu Jai Sid'
# split() method will split string into list of words
print("names.split():", names.split())
# we can also use delimeter. Default delimeter is space
namesDeli = 'Ankit-Shanu-Jai-Sid'
print("names.split('-')", namesDeli.split('-'))

# Convert list to string
namesList  = ['Ankit', 'Shanu', 'Karan', 'Avadh', 'Rajdeep']
print("' '.join():",' '.join(namesList))
print("' '.join():",' * '.join(namesList))

print("Ankit" in namesList)



def tail(t):
    t = t[1:]
    # del t[1:]
    # return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print("letters:", letters)
print('rest:', rest)

vowels = ['a', 'e', 'i', 'o', 'u']
# restVowel = vowels[1:4]
vowels = vowels[1:4]
print("\nvowels:", vowels)
# print("restVowel:", restVowel)
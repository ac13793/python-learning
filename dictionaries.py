import string

print("string.punctuation:", string.punctuation)
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print("counts.keys():", counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])

print("len(counts):", len(counts))

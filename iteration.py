x = 0
x = x + 1
# x++ Python does not support increment/decrement operator
print(x)

for item in range(1, 10):
    print("item:", item)

print("Sum:",sum([1, 2, 3]))

arr = "Ankit, chaurasia"
if not isinstance(arr, list):
    arr = [arr]
print("arr", arr)
print(", ".join(arr))
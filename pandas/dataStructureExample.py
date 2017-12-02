"""This file contains pandas examples"""
import pandas

tbl1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
print(tbl1)
# You can also add columns name
tbl2 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])
print(tbl2)
tbl3 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
print(tbl3)
# You can also pass dictionary
tbl4 = pandas.DataFrame([{"Name": "jhon", "Surname":"peter"}, {"Name": "Mike"}])
print(tbl4)
print("\n**********Mean****************\n",tbl3.mean())
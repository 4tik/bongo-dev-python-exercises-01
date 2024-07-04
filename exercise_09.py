#  Find if 6 available in the list [4, 8, 7, 4,3,6,2,1,9]

numbers =  [4, 8, 7, 4,3,6,2,1,9]
index_number_value = 6
try:
    print(f"value {index_number_value} found in index : {numbers.index(index_number_value)}")
except:
    print(f"value {index_number_value} not found")
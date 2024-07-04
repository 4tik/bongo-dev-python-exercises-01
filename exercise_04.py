# Write a program to find the index of 7
# numbers=[3, 5, 1, 9, 7, 2, 8 ]

numbers=[3, 5, 1, 9, 7, 2, 8]
index_number_value = 70
try:
    print(f"value {index_number_value} index : {numbers.index(index_number_value)}")
except:
    print(f"value {index_number_value} not found")
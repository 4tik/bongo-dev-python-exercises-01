# Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder

def find_elder(first_bro_age=0, second_bro_age=0):
    if(first_bro_age>second_bro_age):
        print(f"first brother is elder, age : {first_bro_age}")
    elif(second_bro_age>first_bro_age):
        print(f"second brother is elder, age : {second_bro_age}")
    else:
        print(f"both are same age : {first_bro_age}")      

first_bro_age=20
second_bro_age=20

find_elder(first_bro_age, second_bro_age)
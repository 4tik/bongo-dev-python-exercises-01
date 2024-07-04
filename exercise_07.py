# FizzBuzz Exercise
# Write a function that takes 1 number as argument.
# The function should return “Fizz” if the number is divisible by 3,
# the function should return “Buzz” if the number is divisible by 5,
# the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
# otherwise return “Not a Fizz-buzz number”
# Hints: Use condition inside the function

def find_fizz_buzz(number=0):
    if(number%3==0 and number%5==0):
        return "FizzBuzz"
    elif(number%3==0):
        return "Fizz"
    elif(number%5==0):
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"    

number = 15
print(find_fizz_buzz(number))
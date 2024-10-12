#!/usr/bin/env python3

def happy_new_year():
    i = 10  # Start the countdown from 10
    while i > 0:  # Loop until i reaches 1
        print(i)  # Print the current value of i
        i -= 1  # Decrement i by 1 after each iteration
    print("Happy New Year!")  # Print after the loop finishes

# Call the function to see the result
happy_new_year()


def square_integers(int_list):
    return [element ** 2 for element in int_list]




def fizzbuzz(num=None):
    if num is None:
        # If no argument is passed, perform the full FizzBuzz for 1 to 100
        for i in range(1, 101):
            print(fizzbuzz(i))
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num



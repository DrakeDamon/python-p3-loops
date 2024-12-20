#!/usr/bin/env python3
# function happyNewYear() {
#   let counter = 10;
#   while (counter > 0) {
#     console.log(counter);
#     counter--;
#   }
#   console.log("Happy New Year!");
# }
def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -=1
    print("Happy New Year!")




# /*
# Write a function `square_integers()` that takes one argument, a list of
# integers and returns the list of squared elements.
# */
# function square_integers(int_list){
#   return int_list.map((num) => Math.pow(num, 2) )
# }
def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num**2)
    return squared_list

# /*
#   Write a method `reverse_string` that takes one argument, a string, and reverses
#   it. Don't use the built-in `.reverse` method. Instead, loop through the
#   characters in the input string and reverse it.
# */
# function reverseString(str) {
#   let reversedStr = "";
#   for (let i = 0; i < str.length; i++) {
#     reversedStr = str[i] + reversedStr;
#   }
#   return reversedStr;
# }
def fizzbuzz():  # Remove the str parameter since we don't need it
    for i in range(1, 101):  # Count from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

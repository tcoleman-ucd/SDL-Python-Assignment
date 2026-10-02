# Exercise 1 By Shreyas Dhumal

# Question:
# Write a program called fizzbuzz.py that generates a sequence from 1 to 100 according to the rules of the FizzBuzz word game so that:
# numbers which are multiples of 3 are replaced by "Fizz";
# numbers which are multiples of 5 are replaced by "Buzz";
# and numbers which are multiples of both 3 and 5 are printed as "FizzBuzz".

# Extensions
# The FizzBuzz game can be extended to multiples of other numbers as well. Extend FizzBuzz program so that (in addition to the previous rules):
# numbers which are multiples of 7 are replaced by "Fang";
# numbers which are multiples of 11 are replaced by "Bang";
# and numbers with multiple factors show the correct combination of words.

############### Main Question with extension #####################

fizzbuzz_list = []
for num in range(1, 101):
    word = ""
    if num % 3 == 0:
        word += "Fizz"  # if number is divisible by 3 it'll replace the number by "Fizz" word
    if num % 5 == 0:
        word += "Buzz"  # It'll add "Buzz" if divisible by 5 and combine with "Fizz" if divisible by 3
    if num % 7 == 0:
        word += "Fang"  # It'll add "Fang" if divisible by 7 and based on the division it'll combine the word
    if num % 11 == 0:
        word += "Bang"  # It'll add "Bang" if divisible by 11 and combine with other matching words.
    if word == "":
        fizzbuzz_list.append(num)  # It'll add the number if the number is not divisible by any condition
    else:
        fizzbuzz_list.append(word)

print(f" FizzBuzz List : {fizzbuzz_list}")

############### Version 1 #####################

# fizzbuzz_list = []
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         fizzbuzz_list.append("FizzBuzz")
#     elif num % 3 == 0:
#         fizzbuzz_list.append("Fizz")
#     elif num % 5 == 0:
#         fizzbuzz_list.append("Buzz")
#     else:
#         fizzbuzz_list.append(num)
# print(f" FizzBuzz List : {fizzbuzz_list}")

################################# END ##############################################

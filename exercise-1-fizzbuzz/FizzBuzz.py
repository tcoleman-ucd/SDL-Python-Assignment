# Exercise 1 Shreyas Dhumal

#Question:
#Write a program called fizzbuzz.py that generates a sequence from 1 to 100 according to the rules of the FizzBuzz word game so that:
# numbers which are multiples of 3 are replaced by "Fizz";
# numbers which are multiples of 5 are replaced by "Buzz";
# and numbers which are multiples of both 3 and 5 are printed as "FizzBuzz".

# Extensions
# The FizzBuzz game can be extended to multiples of other numbers as well. Extend FizzBuzz program so that (in addition to the previous rules):
# numbers which are multiples of 7 are replaced by "Fang";
# numbers which are multiples of 11 are replaced by "Bang";
# and numbers with multiple factors show the correct combination of words.

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
# print(fizzbuzz_list)

############### For extension #####################
fizzbuzz_list = []
for num in range(1,101):
    word = ''
    if num % 3 == 0:
        word += 'Fizz'
    if num % 5 == 0:
        word += 'Buzz'
    if num % 7 == 0:
        word += 'Fang'
    if num % 11 == 0:
        word += 'Bang'
    if word == '':
        fizzbuzz_list.append(num)
    else:
        fizzbuzz_list.append(word)

print(fizzbuzz_list)
# result : [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 'Fang', 8, 'Fizz', 'Buzz', 'Bang', 'Fizz', 13, 'Fang', 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'FizzFang', 'Bang', 23, 'Fizz', 'Buzz', 26, 'Fizz', 'Fang', 29, 'FizzBuzz', 31, 32, 'FizzBang', 34, 'BuzzFang', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'FizzFang', 43, 'Bang', 'FizzBuzz', 46, 47, 'Fizz', 'Fang', 'Buzz', 'Fizz', 52, 53, 'Fizz', 'BuzzBang', 'Fang', 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'FizzFang', 64, 'Buzz', 'FizzBang', 67, 68, 'Fizz', 'BuzzFang', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 'FangBang', 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'FizzFang', 'Buzz', 86, 'Fizz', 'Bang', 89, 'FizzBuzz', 'Fang', 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 'Fang', 'FizzBang', 'Buzz']

################################# END ##############################################
# if word == '':                ## wrong logic
#     fizzbuzz_list.append(num)
# fizzbuzz_list.append(word)
# output : [1, '', 2, '', 'Fizz', 4, '', 'Buzz', 'Fizz', 'Fang', 8, '', 'Fizz', 'Buzz', 'Bang', 'Fizz', 13, '',......]

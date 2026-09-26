import random
#n=10
li = random.randint(1, 20)#generate random numbers, but with a range
power= random.choice([2,3])
j = li**power
#Function that squares the numbers
# def square(n):
#     list=[]
#     for i in n:
#         list.append(i**2)
#     return list

#Function that cubes the numbers:
# def cube(n):
#     list=[]
#     for i in n:
#         list.append(i**3)
#     return list

# while True
#     j = li**power
#     if j


num = random.randint(1, 20)
power = random.choice([2,3])
result = li**power
pre_result = 0
while True:
    new_result= result
    
    if new_result%pre_result==0:
        break


    prev_result = new_result
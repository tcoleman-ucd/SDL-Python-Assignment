import random
n=10
li = [random.randint(1, 20) for _ in range(n)] #generate random numbers, but with a range
print(li)

#Function that squares the numbers
def square(n):
    list=[]
    for i in n:
        list.append(i**2)
    return list

#Function that cubes the numbers:
def cube(n):
    list=[]
    for i in n:
        list.append(i**3)
    return list

print(square(li))
print(cube(li))
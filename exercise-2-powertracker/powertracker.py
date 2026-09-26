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
pre_result = num**power
list = []
count = 0
while True:
    num = random.randint(1, 20)
    power = random.choice([2,3])
    result = num**power
    
    if (pre_result%result)!=0:
        count += 1
        pre_result = result
        list.append(result)
        continue
        
    if (pre_result%result)==0:
        print(f"this is count {count}")
        print(f"{pre_result} and {result}")
        break
        
    
print(list)
print(max(list))
print(min(list))
    


###Valeria Trijueque

import random #Import random library

list = [] #Initialize a list
count = 0 #Initialize a count
pre_result = 0 #Initialize the previouse result

#While loop
while True:
    num = random.randint(1, 20)#random number between 1 and 20
    power = random.choice([2,3]) #random choice between square or cube the number
    result = num**power #create random numbers and then randomly square them or cube them

    if pre_result ==0: # if the previouse result is equal to zero continue, because we cannot devide a number by zero
        pre_result = result #update the previouse result
        continue

    if  (result%pre_result)==0 and pre_result!=1:#if the current result is divisible by the previouse result #+extension (if the previous number is *not* 1)
        count += 1 #add the count to the loop or iteration
        list.append(result)
        print(f"Lop {count}: {num}^{power} = {result}") #print values
        break #stop while loop

    else: # if the current result is not divisible by the previouse result, meaning that the remainder is not 0
        count += 1 #add the count of the loop or iteration
        pre_result = result #update the previouse result
        list.append(result) #store results to the list
        print(f"Lop {count}: {num}^{power} = {result}") #print values
        continue # go back to the start of the loop
        
#print values
print(f"The largest result is {max(list)}") 
print(f"The smallest result is {min(list)}")
print(f"{pre_result} is divisible by {result}")
print(f"We completed {count} loops")

#Valeria Trijueque

import random #Import random library
#from sys import 

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

num = random.randint(1, 20) #Make random numbers from 1 to 20
power = random.choice([2,3]) #Choose between square or cube
pre_result = num**power #Create the first previous result
list = [] #Initialize a list
count = 0 #Initialize a count

#While loop
while True:
    num = random.randint(1, 20)
    power = random.choice([2,3])
    result = num**power #create random numbers and then randomly square them or cube them
    
    if  (result%pre_result)==0 and pre_result!=1:#else if the current result is divisible by the previouse result #+extension (if the previous number is *not* 1)
        count += 1 #add the count to the loop or iteration
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

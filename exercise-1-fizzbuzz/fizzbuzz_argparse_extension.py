##Valeria Trijueque (Shreyas code from exercise one + extension Command line arguments & `argparse`)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--factorword', nargs = 2, action= 'append') # argument: factor and word (allow the user to add as many as they want)
parser.add_argument('--maxnum', type = int) # argument: maximum number 
#parser.add_argument('--word', type = str)

args = parser.parse_args()

#create an empty list to put all the factor and words input by the user into a list 
lsit=[]
for f in args.factorword:
    lsit += [[f[0], f[1]]]

def fizzbuzz(list, N):
    #create an empty list to later store the solution
    fizzbuzz_list = []
    #loop over the ammount of numbers specified by the user
    for num in range(1, N+1):
            wordnum = ""
            #loop over the factors and words input by the user 
            for val in list:
                    factor = int(val[0])
                    word= str(val[1])
                    if num % factor == 0:
                        wordnum += word          
            #keep outside the loop so it can print the last value (if it is kept inside the loop
            # it will output e.g: 1,1, buzz, buzzbizz. And if it is outside it will output: 1, buzzbizz).      
            if wordnum == "":
                fizzbuzz_list.append(num)  # It'll add the number if the number is not divisible by any condition
            else:
                fizzbuzz_list.append(wordnum) #Add the word or words if the number is divisible by one or more conditions
    return fizzbuzz_list
    

if __name__ == '__main__':
    f =  fizzbuzz(lsit, args.maxnum)
    print(f" FizzBuzz List : {f}")
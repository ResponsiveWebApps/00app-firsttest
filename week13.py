def gensquares(N):
    output = []

    for i in range(N):
        my_input = i * i 
        output.append(my_input)
    
    return output

#for x in gensquares(10):
#    print(x)


import random

def rand_num(low,high,n):
    output = []

    for i in range(n):
        my_input = random.randrange(low,high)
        output.append(my_input)
    
    return output

    

for num in rand_num(1,10,12):
    print(num)
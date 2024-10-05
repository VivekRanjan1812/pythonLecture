# Write a function to count n and evaluate a = n * 10 for all values from import time

import time

def count(n):
    for i in range(0,n):
        a = n * 10
ns = [100000 ,234234 , 34345 , 345 , 344 , 345] 
# n = 1000000       
# code to evaluate run time of function call count(n)        
start_time = time.time()
print(start_time ) 
count(1000000)
end_time = time.time()
# print(end_time)    

print(f"\n n=(n)Time to execute is {end_time - start}")   
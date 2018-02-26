#############################################################################
# HARDNESS OF FACTORING EXPERIMENT CODE
# CS Core: Hardness and Complexity
#############################################################################

import time #For keepin track of how long it takes to factor N
import math #For taking the square root of N

N = 0 #Insert your choice of N here

factors = [] #List of factors, empty to start

start = time.time() #Start the timer

for num in range(1, int(math.sqrt(N)) + 1): #For all numbers from 1 to the square root of N:

    if N%num == 0: #If the number divides N (i.e. if the remainder of N/i is 0),

        factors.append(num) #Add below sqrt(N) factor to factors list

        factors.append(N/num) #Add above sqrt(N) factor to factors list

stop = time.time() #Stop the timer

print "FACTORS of ", N, ": ", factors
print "TIME ELAPSED: ", stop - start




    

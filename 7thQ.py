import math

def primecheck(number):
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    else: return True

print(primecheck(11))

primelist=[]
i =2
while True:
    if len(primelist)==10001:
        print(primelist[-1])
        break
    if primecheck(i):
        primelist.append(i)
        i = i+1
    else:
        i = i+1

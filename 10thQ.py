import math

summary = 0
for i in range(2,2000000):
    for j in range(2,int( math.sqrt(i))+1):
        if i%j ==0:
            break
    else:
        summary+=i
print(summary)
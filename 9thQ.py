import math

for i in range(1,1000):
    for j in range(1,1000):
        k = i**2 + j**2
        k_sqrt = math.sqrt(k)
        if int(k_sqrt)==k_sqrt:
            if (k_sqrt+i+j)==1000:
                print(i,j,k_sqrt)
                break











def divisible(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

numberlist= [i for i in range(2,1000)]
print(numberlist)
summary=0
for i in numberlist:
    if divisible(i):
        summary +=i
print(summary)






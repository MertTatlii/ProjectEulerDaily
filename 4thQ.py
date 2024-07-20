#4. QUESTİON--------------------------------------------
number = "125648"
print(number)
number = number[::-1]
print(number)

maxnum=998001
minnum=10000
liste=[]
for i in range(999,100,-1):
    for j in range(999,i,-1):
        num = str(i*j)
        if num==num[::-1]:
            liste.append(i*j)
            break
print(max(liste))
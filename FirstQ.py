#Project Euler 3. QUESTİON---------------------------------------------------------
# #600851475143
# import math
# def primecheck(x):
#     is_prime =True
#
#     for i in range(2,int(math.sqrt(x))+1):
#         if x %i ==0:
#             is_prime=False
#             continue
#     return is_prime
# number = 600851475143
# biggest_prime = 1
# for i in range(2,int(math.sqrt(number))):
#     if number %i == 0 and primecheck(i)== True:
#         biggest_prime=i
# print(biggest_prime)
#aksdjasf

#4. QUESTİON--------------------------------------------
# number = "125648"
# print(number)
# number = number[::-1]
# print(number)

# maxnum=998001
# minnum=10000
# liste=[]
# for i in range(999,100,-1):
#     for j in range(999,i,-1):
#         num = str(i*j)
#         if num==num[::-1]:
#             liste.append(i*j)
#             break
# print(max(liste))

#5. QUESTİON-------------------------------------------------
# import math
# import functools
# def gcd(x,y):
#     return math.gcd(x,y)
# def lcm(x,y):
#     return math.lcm(x,y)
# #gcd ebob, lcm ekok demektir.
# liste = range(1,21)
# sonuc=functools.reduce(lcm,liste)
# print(sonuc)


#6. QUESTİON------------------------------------------------------
# import functools
#
# def sum(x,y):
#     return x+y
# def square(x):
#     return x**2
# numbers= range(1,101)
# summary= functools.reduce(sum,numbers)
# print(summary)
# squaresummary=0
# for i in numbers:
#     squaresummary= squaresummary+square(i)
# print(squaresummary)
# result= summary*summary-squaresummary
# print(f"result is: {result}")
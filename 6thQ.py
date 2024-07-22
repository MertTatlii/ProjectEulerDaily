# 6. QUESTİON------------------------------------------------------
import functools

def sum(x,y):
    return x+y
def square(x):
    return x**2
numbers= range(1,101)
summary= functools.reduce(sum,numbers)
print(summary)
squaresummary=0
for i in numbers:
    squaresummary= squaresummary+square(i)
print(squaresummary)
result= summary*summary-squaresummary
print(f"result is: {result}")
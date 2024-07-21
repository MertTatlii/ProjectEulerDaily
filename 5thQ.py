#5. QUESTİON-------------------------------------------------
import math
import functools
def gcd(x,y):
    return math.gcd(x,y)
def lcm(x,y):
    return math.lcm(x,y)
#gcd ebob, lcm ekok demektir.
liste = range(1,21)
sonuc=functools.reduce(lcm,liste)
print(sonuc)
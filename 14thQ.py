# number = 1000000
# loopnum = 999999
# print(number)
# maxloop = 0
# loopcount = 0
# while True:
#     loopnum = loopnum-1
#     while True:
#         if number == 1:
#             loopcount +=1
#             break
#         elif number % 2 == 0:
#             number = number/2
#             loopcount += 1
#         else:
#             number = (3*number)+1
#             loopcount += 1
#     if loopcount> maxloop:
#         maxloop = loopcount
#     elif loopnum == 1:
#         break
# print(maxloop)



def collatz(x):
    adim = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        adim += 1
    return adim

max_sayi = 0
max_adim = 0
for sayi in range(2,1000001):
    sonuc = collatz(sayi)
    if sonuc > max_adim:
        max_adim = sonuc
        max_sayi = sayi

print(f"{max_sayi} sayısı : {max_adim} adım üretti.")

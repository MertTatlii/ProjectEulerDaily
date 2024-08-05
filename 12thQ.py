# #Triangular number
#
# def bolunebilme(sayi):
#     bolenler = []
#     for i in range(1,sayi):
#         if sayi % i == 0:
#             bolenler.append(i)
#     return bolenler
#
# i = 1
# while True:
#
#     bolenler = bolunebilme(i)
#     if len(bolenler)>19:
#         if i == sum(bolenler):
#             print(i)
#             break
#     i = i+1

n = 1
while True:
    bolen_sayisi = 1
    ucgensel_sayi = int((n*(n+1))/2)
    for i in range(2, int((ucgensel_sayi**0.5)+1)):
        if ucgensel_sayi % i == 0:
            bolen_sayisi += 1
    n += 1
    bolen_sayisi *= 2
    if bolen_sayisi > 500:
                print(ucgensel_sayi)
                break


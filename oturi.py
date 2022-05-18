pricelist = []

#入力をリストに格納
for i in range(0, 5):
    val = 1000 - int(input())
    if val == 1000:
        break

    if val:
        pricelist.append(val)

count = 0
oturi = 0
coin_list = [500, 100, 50, 10, 5, 1]
oturi_list = []


#貪欲法によって500円から順に確認する
for i, price_notuse in enumerate(pricelist):
    for coin in coin_list:
        if pricelist[i] / coin >= 1:
            count = pricelist[i] // coin
            oturi += pricelist[i] // coin
            pricelist[i] -= (count * coin)
            count = 0
    
    if oturi:
        oturi_list.append(oturi)
        oturi = 0

for item in oturi_list:
    print(item)
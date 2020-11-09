import math
from random import *
import random
import copy
import pandas as pd
import numpy as np
from random import (choice, random, randint)
import time

start_time = time.time()

"""
평균 3일치 수요
"""
#blk_demand = [90000, 85000, 87000]  # 외주로 나가는 blk 완성 item 별 수요
#prs_demand = [15000, 14000, 13000, 15000]  # 외주로 나가는 prs 완성 item 별 수요
#asy_demand = [180, 170]  # 외주로 나가는 asy 완성 item 별 수요

"""
평균 1일치 수요
"""
blk_demand = [30000, 28000, 29000]  # 외주로 나가는 blk 완성 item 별 수요
prs_demand = [5000, 4800, 4600, 5200]  # 외주로 나가는 prs 완성 item 별 수요
asy_demand = [55, 65]  # 외주로 나가는 asy 완성 item 별 수요

"""
평균 2일치 수요
"""
#blk_demand = [60000, 62000, 58000]  # 외주로 나가는 blk 완성 item 별 수요
#prs_demand = [10000, 11000, 9000, 10000]  # 외주로 나가는 prs 완성 item 별 수요
#asy_demand = [130, 110]  # 외주로 나가는 asy 완성 item 별 수요

"""
평균 4일치 수요
"""
#blk_demand = [120000, 115000, 125000]  # 외주로 나가는 blk 완성 item 별 수요
#prs_demand = [20000, 21000, 19000, 21000]  # 외주로 나가는 prs 완성 item 별 수요
#asy_demand = [250, 230]  # 외주로 나가는 asy 완성 item 별 수요

coil_capa = 100000  # coil 보관장 면적
blk_capa = 100000  # blk 보관장 면적
prs_capa = 100000  # prs 보관장 면적
asy_capa = 100000  # asy 보관장 면적

productioncost = [500, 1, 6, 420]  # 공정 생산 가격
setupcost = [2700, 900, 900, 1800]
holdcost = [3, 3, 15, 51]  # 공정 재고 유지 가격
ordercost = [4500, 4500, 900, 270]  # 공정 주문 비용

# setupcost = [10, 6, 5, 2]
# holdcost = [1, 3, 5, 7]  # 공정 재고 유지 가격
# ordercost = [100, 200, 300, 400]  # 공정 주문 비용

"""
coil_inventory = [2, 3]  # 보관장 coil 재고
blk_inventory = [500, 400, 800]  # 보관장 blk 재고
prs_inventory = [200, 300, 100, 100]  # 보관장 prs 재고
asy_inventory = [50, 50]  # 보관장 asy 재고
"""

"안전재고 0일때 0번째 T 끝났을 때 재고"
coil_inventory = [60, 55]  # 보관장 coil 재고
blk_inventory = [30000, 28000, 29000]  # 보관장 blk 재고
prs_inventory = [4800, 5000, 4900, 4700]  # 보관장 prs 재고
asy_inventory = [60, 50]  # 보관장 asy 재고

"안전재고 0 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [60, 47]  # 보관장 coil 재고
#blk_inventory = [0, 0, 1000]  # 보관장 blk 재고
#prs_inventory = [1300, 1500, 900, 200]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 0 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [0, 3]  # 보관장 coil 재고
#blk_inventory = [0, 0, 1000]  # 보관장 blk 재고
#prs_inventory = [300, 500, 900, 200]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고

"안전재고 1 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [32, 31]  # 보관장 coil 재고
#blk_inventory = [16000, 16000, 15000]  # 보관장 blk 재고
#prs_inventory = [3300, 3500, 2900, 2700]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 1 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [32, 31]  # 보관장 coil 재고
#blk_inventory = [16000, 16000, 15000]  # 보관장 blk 재고
#prs_inventory = [4300, 2500, 2900, 2700]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고

"안전재고 2 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [60, 59]  # 보관장 coil 재고
#blk_inventory = [30000, 30000, 29000]  # 보관장 blk 재고
#prs_inventory = [5300, 5500, 4900, 5200]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 2 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [60, 59]  # 보관장 coil 재고
#blk_inventory = [30000, 30000, 29000]  # 보관장 blk 재고
#prs_inventory = [6300, 6500, 4900, 5200]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고

"안전재고 3 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [88, 87]  # 보관장 coil 재고
#blk_inventory = [44000, 44000, 45000]  # 보관장 blk 재고
#prs_inventory = [7300, 7500, 8900, 7700]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 3 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [88, 87]  # 보관장 coil 재고
#blk_inventory = [44000, 44000, 45000]  # 보관장 blk 재고
#prs_inventory = [8300, 8500, 8900, 7700]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고

"안전재고 4 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [120, 119]  # 보관장 coil 재고
#blk_inventory = [58000, 58000, 59000]  # 보관장 blk 재고
#prs_inventory = [11300, 11500, 10900, 9700]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 4 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [120, 119]  # 보관장 coil 재고
#blk_inventory = [58000, 58000, 59000]  # 보관장 blk 재고
#prs_inventory = [10300, 10500, 10900, 9700]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고

"안전재고 5 일때 1번째 T 끝났을 때 재고"
#coil_inventory = [148, 147]  # 보관장 coil 재고
#blk_inventory = [74000, 74000, 73000]  # 보관장 blk 재고
#prs_inventory = [13300, 13500, 12900, 12200]  # 보관장 prs 재고
#asy_inventory = [460, 450]  # 보관장 a1sy 재고

"안전재고 5 일때 2번째 T 끝났을 때 재고"
#coil_inventory = [148, 147]  # 보관장 coil 재고
#blk_inventory = [74000, 74000, 73000]  # 보관장 blk 재고
#prs_inventory = [12300, 12500, 12900, 12200]  # 보관장 prs 재고
#asy_inventory = [260, 250]  # 보관장 a1sy 재고


"""
coil_inventory = [180, 165]  # 보관장 coil 재고
blk_inventory = [90000, 84000, 87000]  # 보관장 blk 재고
prs_inventory = [14400, 15000, 14700, 14100]  # 보관장 prs 재고
asy_inventory = [180, 150]  # 보관장 asy 재고
"""
"""
coil_inventory = [120, 110]  # 보관장 coil 재고
blk_inventory = [60000, 56000, 58000]  # 보관장 blk 재고
prs_inventory = [9600, 10000, 9800, 9400]  # 보관장 prs 재고
asy_inventory = [120, 100]  # 보관장 asy 재고
"""
"""
coil_inventory = [0, 0]  # 보관장 coil 재고
blk_inventory = [0, 0, 0]  # 보관장 blk 재고
prs_inventory = [0, 0, 0, 0]  # 보관장 prs 재고
asy_inventory = [0, 0]  # 보관장 asy 재고
"""

T = 100000  # planning horizon

productionrate = [1, 10, 10, 5]  # 공정별 생산률
penalty_delivery = [0, 3, 5, 7]  # 공정별 미납 페널티
penalty_ss = [10, 10, 10, 10]  # 공정별 안전재고 미달 페널티

parents = []
popsize = 20


def divisor(a):
    divisors = []
    t_num = int(a / 2)

    divisors.append(a)
    while t_num >= 1:
        if a % t_num == 0:
            divisors.append(t_num)
        t_num -= 1

    return divisors


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def initial(popssize):
    parents = []
    s1 = 0
    s2 = 0
    c1 = 0
    c2 = 0
    a = []  # asy demand 1의 약수
    b = []  # asy demand 2의 약수
    w = []
    for i in range(popsize):
        k40 = 0
        k41 = 0
        k42 = 0
        k43 = 0

        lot_size = [0, 0, 0, 0]
        k1 = [0, 0]
        k2 = [0, 0, 0]
        k3 = [0, 0, 0, 0]
        k4 = [0, 0, 0, 0]
        m1 = [0, 0]
        m2 = [0, 0, 0, 0, 0, 0]
        m3 = [0, 0, 0, 0, 0, 0, 0, 0]
        m4 = [0, 0]
        safetystock = [0, 0, 0, 0]
        #safetystock = [29, 14500, 2415, 30]
        #afetystock = [58, 29000, 4830, 60]
        #safetystock = [87, 43500, 7245, 90]
        #safetystock = [118, 58000, 9660, 120]
        #safetystock = [145, 72500, 12075, 150]

        c = asy_demand[0] + safetystock[3]  # 앞 공정에서 c만큼 생산되어야 함
        d = asy_demand[1] + safetystock[3]  # 앞 공정에서 d만큼 생산되어야 함
        a.append(divisor(c))
        b.append(divisor(d))

        #z = gcd(c, d)  # z 는 asy demand들의 최대 공약수
        z = randrange(10,101,10)

        lot_size[3] = z

        m4[0] = asy_demand[0] / lot_size[3]
        m4[1] = asy_demand[1] / lot_size[3]

        for i in range(len(m4)):
            if int(m4[i]) == m4[i]:
                m4[i] = m4[i]
            else:
                m4[i] = int(m4[i]) + 1


        a1 = m4[0] * z
        a2 = m4[1] * z

        k4[0] = (a1 + safetystock[3] - asy_inventory[0]) / lot_size[3]
        k4[1] = k4[0]
        k4[2] = (a2 + safetystock[3] - asy_inventory[1]) / lot_size[3]
        k4[3] = k4[2]

        lot_size[2] = randrange(2*lot_size[3], 5001, lot_size[3])

        lot_size[1] = randrange(lot_size[2] , 30001 , lot_size[2])

        ra = lot_size[1] / lot_size[2]
        if int(lot_size[1] / 500) == lot_size[1] / 500 :
            lot_size[1] = lot_size[1]
        else :
            lot_size[1] = (int(lot_size[1] / 500) + 1) * 500

        if int(lot_size[1] / lot_size[2] ) == lot_size[1] / lot_size[2] :
            lot_size[2] = lot_size[2]
        else:
            if int(lot_size[1] / ra) == lot_size[1] / ra :
                lot_size[2] = lot_size[1] / ra
                if lot_size[2] % 10 != 0:
                    lot_size[2] = lot_size[1] / ra * 2
            else :
                while True :
                    ra += 1
                    lot_size[2] = lot_size[1] / ra
                    if int(lot_size[2]) == lot_size[2] :
                        lot_size[2] = lot_size[2]
                        if lot_size[2] % 10 != 0 :
                            continue
                        else :
                            break

        if int(lot_size[2] / lot_size[3]) == lot_size[2] / lot_size[3] :
            lot_size[3] = lot_size[3]
        else :
            for z in range(100, 9, -10):
                if int(lot_size[2] / z) == lot_size[2] / z:
                    lot_size[3] = z
                    break

        m3[0] = (a1 + safetystock[3]) / lot_size[2]
        m3[1] = (a1 + safetystock[3]) / lot_size[2]
        m3[2] = (a2 + safetystock[3]) / lot_size[2]
        m3[3] = (a2 + safetystock[3]) / lot_size[2]
        m3[4] = prs_demand[0] / lot_size[2]
        m3[5] = prs_demand[1] / lot_size[2]
        m3[6] = prs_demand[2] / lot_size[2]
        m3[7] = prs_demand[3] / lot_size[2]

        for i in range(len(m3)):
            if int(m3[i]) == m3[i]:
                m3[i] = m3[i]
            else:
                m3[i] = int(m3[i]) + 1

        b1 = (m3[2] + m3[6]) * lot_size[2]
        b2 = (m3[1] + m3[5]) * lot_size[2]
        b3 = (m3[3] + m3[7]) * lot_size[2]
        b4 = (m3[0] + m3[4]) * lot_size[2]

        k3[0] = (b1 + safetystock[2]) / lot_size[2]
        k3[1] = (b2 + safetystock[2]) / lot_size[2]
        k3[2] = (b3 + safetystock[2]) / lot_size[2]
        k3[3] = (b4 + safetystock[2]) / lot_size[2]

        m2[0] = k3[0] / lot_size[1]
        m2[1] = k3[1] / lot_size[1]
        m2[2] = k3[2] / lot_size[1]
        m2[3] = blk_demand[0] / lot_size[1]
        m2[4] = blk_demand[1] / lot_size[1]
        m2[5] = blk_demand[2] / lot_size[1]

        k2[0] = ((m2[1] + m2[4]) * lot_size[1] + safetystock[1]) / lot_size[1]
        k2[1] = ((m2[0] + m2[3]) * lot_size[1] + safetystock[1]) / lot_size[1]
        k2[2] = ((m2[2] + m2[5]) * lot_size[1] + safetystock[1]) / lot_size[1]

        m1[0] = k2[0]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생
        m1[1] = k2[1]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생

        lot_size[0] = lot_size[1] / 500

        k1[0] = m1[0] + safetystock[0]
        k1[1] = m1[1] + safetystock[0]

        parent = []
        parent.append(lot_size)
        parent.append(k1)
        parent.append(k2)
        parent.append(k3)
        parent.append(k4)
        parent.append(m1)
        parent.append(m2)
        parent.append(m3)
        parent.append(m4)
        parent.append(safetystock)
        parents.append(parent)

    return parents

#print(initial(popsize))


def inifs(popsize):
    a = initial(popsize)

    for i in range(len(a)):
        pencost = 0
        lot_size = []
        k1 = []
        k2 = []
        k3 = []
        k4 = []
        m1 = []
        m2 = []
        m3 = []
        m4 = []
        safetystock = []

        lot_size = a[i][0]
        k1 = a[i][1]
        k2 = a[i][2]
        k3 = a[i][3]
        k4 = a[i][4]
        m1 = a[i][5]
        m2 = a[i][6]
        m3 = a[i][7]
        m4 = a[i][8]
        safetystock = a[i][9]

        for j in range(len(k1)):
            if int(k1[j]) == k1[j]:
                k1[j] = k1[j]
            else:
                k1[j] = int(k1[j]) + 1

        for j in range(len(m1)):
            if int(m1[j]) == m1[j]:
                m1[j] = m1[j]
            else:
                m1[j] = int(m1[j]) + 1

        while True:
            if safetystock[0] > (coil_inventory[0] + lot_size[0] * (k1[0] - m1[0])):
                if k1[0] <= 300:
                    k1[0] += 1
                else:
                    k1[0] = 300
                    pencost += (safetystock[0] - (coil_inventory[0] + lot_size[0] * (k1[0] - m1[0]))) * penalty_ss[0]
            else:
                pencost += 0
                break

        while True:
            if safetystock[0] > (coil_inventory[1] + lot_size[0] * (k1[1] - m1[1])):
                if k1[1] <= 300:
                    k1[1] += 1
                else:
                    pencost += (safetystock[0] - (coil_inventory[1] + lot_size[0] * (k1[1] - m1[1]))) * penalty_ss[0]
            else:
                pencost += 0
                break

        k2[0] = (m1[0] + (safetystock[1]-blk_inventory[0]) / lot_size[1])
        k2[1] = (m1[1] + (safetystock[1]-blk_inventory[1]) / lot_size[1])
        k2[2] = m2[2] + m2[5] + (safetystock[1]-blk_inventory[2])/ lot_size[1]

        for j in range(len(k2)):
            if int(k2[j]) == k2[j]:
                k2[j] = k2[j]
            else:
                k2[j] = int(k2[j])

        for j in range(len(m2)):
            if int(m2[j]) == m2[j]:
                m2[j] = m2[j]
            else:
                m2[j] = int(m2[j]) + 1

        while True:
            if safetystock[1] >= blk_inventory[0] + lot_size[1] * (k2[0] - m2[1] - m2[4]):
                k2[0] += 1
            else:
                break

        while True:
            if safetystock[1] >= blk_inventory[1] + lot_size[1] * (k2[1] - m2[0] - m2[3]):
                k2[1] += 1
            else:
                break

        while True:
            if safetystock[1] >= blk_inventory[2] + lot_size[1] * (k2[2] - m2[2] - m2[5]):
                k2[2] += 1
            else:
                break

        k3[0] = (m2[0] + safetystock[2] / lot_size[2])
        k3[1] = (m2[1] + safetystock[2] / lot_size[2])
        k3[2] = (m2[2] + safetystock[2] / lot_size[2])

        for j in range(len(k3)):
            if int(k3[j]) == k3[j]:
                k3[j] = k3[j]
            else:
                k3[j] = int(k3[j]) + 1

        for j in range(len(m3)):
            if int(m3[j]) == m3[j]:
                m3[j] = m3[j]
            else:
                m3[j] = int(m3[j]) + 1

        while True:
            if safetystock[2] >= prs_inventory[0] + lot_size[2] * (k3[0] - m3[2] - m3[6]):
                k3[0] += 1
            else:
                break

        while True:
            if safetystock[2] >= prs_inventory[1] + lot_size[2] * (k3[1] - m3[1] - m3[5]):
                k3[1] += 1
            else:
                break

        while True:
            if safetystock[2] >= prs_inventory[2] + lot_size[2] * (k3[2] - m3[3] - m3[7]):
                k3[2] += 1
            else:
                break

        while True:
            if safetystock[2] >= prs_inventory[3] + lot_size[2] * (k3[3] - m3[0] - m3[4]):
                k3[3] += 1
            else:
                break

        k4[0] = m3[0] + safetystock[3] / lot_size[3]
        k4[1] = m3[1] + safetystock[3] / lot_size[3]
        k4[2] = m3[2] + safetystock[3] / lot_size[3]
        k4[3] = m3[3] + safetystock[3] / lot_size[3]

        if k4[0] >= k4[1]:
            k4[0] = k4[1]
        else:
            k4[1] = k4[0]

        if k4[2] >= k4[3]:
            k4[2] = k4[3]
        else:
            k4[3] = k4[2]

        for j in range(len(k4)):
            if int(k4[j]) == k4[j]:
                k4[j] = k4[j]
            else:
                k4[j] = int(k4[j]) + 1

        m4[0] = asy_demand[0] / lot_size[3]
        m4[1] = asy_demand[1] / lot_size[3]

        for j in range(len(m4)):
            if int(m4[j]) == m4[j]:
                m4[j] = m4[j]
            else:
                m4[j] = int(m4[j]) + 1

        while True:
            if safetystock[3] >= asy_inventory[0] + lot_size[3] * (k4[0] - m4[0]):
                k4[0] += 1
                k4[1] = k4[0]
            else:
                break

        while True:
            if safetystock[3] >= asy_inventory[1] + lot_size[3] * (k4[2] - m4[1]):
                k4[2] += 1
                k4[3] = k4[2]
            else:
                break

        c = asy_demand[0] - asy_inventory[0] + safetystock[3]  # 앞 공정에서 c만큼 생산되어야 함
        d = asy_demand[1] - asy_inventory[1] + safetystock[3]  # 앞 공정에서 d만큼 생산되어야 함

        a1 = m4[0] * lot_size[3]
        a2 = m4[1] * lot_size[3]

        lot_size[3] = randrange(10, 101, 10)
        if int(lot_size[2] / lot_size[3]) == lot_size[2] / lot_size[3]:
            lot_size[3] = lot_size[3]
        else:
            for i in range(10, 101, 10):
                if int(lot_size[2] / i) == lot_size[2] / i:
                    lot_size[3] = i
                    break

        m3[0] = k4[0] * lot_size[3] / lot_size[2]
        m3[1] = k4[1] * lot_size[3] / lot_size[2]
        m3[2] = k4[2] * lot_size[3] / lot_size[2]
        m3[3] = k4[3] * lot_size[3] / lot_size[2]
        m3[4] = prs_demand[0] / lot_size[2]
        m3[5] = prs_demand[1] / lot_size[2]
        m3[6] = prs_demand[2] / lot_size[2]
        m3[7] = prs_demand[3] / lot_size[2]

        for i in range(len(m3)):
            if int(m3[i]) == m3[i]:
                m3[i] = m3[i]
            else:
                m3[i] = int(m3[i]) + 1

        k4[0] = m3[0] * lot_size[2] / lot_size[3]
        k4[1] = k4[0]
        k4[2] = m3[2] * lot_size[2] / lot_size[3]
        k4[3] = k4[2]
        for j in range(len(k4)):
            if int(k4[j]) == k4[j]:
                k4[j] = k4[j]
            else:
                k4[j] = int(k4[j]) + 1

        b1 = (m3[2] + m3[6]) * lot_size[2] + safetystock[2]
        b2 = (m3[1] + m3[5]) * lot_size[2] + safetystock[2]
        b3 = (m3[3] + m3[7]) * lot_size[2] + safetystock[2]
        b4 = (m3[0] + m3[4]) * lot_size[2] + safetystock[2]

        m2[0] = b1 / lot_size[1]
        m2[1] = b2 / lot_size[1]
        m2[2] = b3 / lot_size[1]
        m2[3] = blk_demand[0] / lot_size[1]
        m2[4] = blk_demand[1] / lot_size[1]
        m2[5] = blk_demand[2] / lot_size[1]

        for i in range(len(m2)):
            if int(m2[i]) == m2[i]:
                m2[i] = m2[i]
            else:
                m2[i] = int(m2[i]) + 1

        if int(m3[2]) == m3[2] or int(m3[6]) == m3[6]:
            k3[0] = m3[2] + m3[6] + (safetystock[2] - prs_inventory[0]) / lot_size[2]
        else:
            k3[0] = (int(m3[2]) + int(m3[6]))

        if int(m3[1]) == m3[1] or int(m3[5]) == m3[5]:
            k3[1] = m3[1] + m3[5] + (safetystock[2] - prs_inventory[1]) / lot_size[2]
        else:
            k3[1] = (int(m3[1]) + int(m3[5]))

        if int(m3[3]) == m3[3] or int(m3[7]) == m3[7]:
            k3[2] = m3[3] + m3[7] + (safetystock[2] - prs_inventory[2]) / lot_size[2]
        else:
            k3[2] = (int(m3[3]) + int(m3[7]))

        if k3[0] * lot_size[2] != lot_size[1] * m2[0] :
            k3[0] = m2[0] * lot_size[1] / lot_size[2]
        if k3[1] * lot_size[2] != lot_size[1] * m2[1] :
            k3[1] = m2[1] * lot_size[1] / lot_size[2]
        if k3[2] * lot_size[2] != lot_size[1] * m2[2] :
            k3[2] = m2[2] * lot_size[1] / lot_size[2]


        #k3[0] = m3[2] + m3[6] +(safetystock[2] - prs_inventory[0]) / lot_size[2]
        #k3[1] = m3[1] + m3[5] + (safetystock[2] - prs_inventory[1]) / lot_size[2]
        #k3[2] = m3[3] + m3[7] + (safetystock[2] - prs_inventory[2]) / lot_size[2]
        k3[3] = m3[0] + m3[4] + (safetystock[2] - prs_inventory[3] ) / lot_size[2]

        k2[0] = (m1[0] + (safetystock[1]-blk_inventory[0]) / lot_size[1])
        k2[1] = (m1[1] + (safetystock[1]-blk_inventory[1]) / lot_size[1])

        if int(m2[1]) == m2[1] or int(m2[4]) == m2[4]:
            k2[0] = m2[1] + m2[4] + (safetystock[1]-blk_inventory[0]) / lot_size[1]
        else:
            k2[0] = (int(m2[1]) + int(m2[4]) + 2)

        if int(m2[0]) == m2[0] or int(m2[3]) == m2[3]:
            k2[1] = m2[0] + m2[3] + (safetystock[1]-blk_inventory[1]) / lot_size[1]
        else:
            k2[1] = (int(m2[0]) + int(m2[3]) + 2) + safetystock[1] / lot_size[1]

        k2[2] = m2[2] + m2[5] + (safetystock[1] - blk_inventory[2]) / lot_size[1]

        m1[0] = k2[0]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생
        m1[1] = k2[1]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생

        """
        k1 식 작성하기 .. 
        """
        k1[0] = m1[0] + safetystock[0]
        k1[1] = m1[1] + safetystock[0]
        if k1[0] < 0:
            k1[0]

        for i in range(len(k1)):
            if int(k1[i]) == k1[i]:
                k1[i] = k1[i]
            else:
                k1[i] = int(k1[i]) + 1

        for i in range(len(k2)):
            if int(k2[i]) == k2[i]:
                k2[i] = k2[i]
            else:
                k2[i] = int(k2[i]) + 1

        for i in range(len(k3)):
            if int(k3[i]) == k3[i]:
                k3[i] = k3[i]
            else:
                k3[i] = int(k3[i]) + 1

        for i in range(len(k4)):
            if int(k4[i]) == k4[i]:
                k4[i] = k4[i]
            else:
                k4[i] = int(k4[i]) + 1

        for i in range(len(m1)):
            if int(m1[i]) == m1[i]:
                m1[i] = m1[i]
            else:
                m1[i] = int(m1[i]) + 1

        for i in range(len(m3)):
            if int(m3[i]) == m3[i]:
                m3[i] = m3[i]
            else:
                m3[i] = int(m3[i]) + 1

        for i in range(len(m4)):
            if int(m4[i]) == m4[i]:
                m4[i] = m4[i]
            else:
                m4[i] = int(m4[i]) + 1
    return a


"""
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
pop size 1개에서는 제약도 성립하게끔 짜놈 ..
2개 이상으로 가면 이상하게 됨 .. 이것 해결해야 된다.
"""

#print(inifs(popsize))

def fitness(parents, popsize):  # popsize가 다 들어가는 것이 아니고 1개만 들어가게 해야 된다 .
    parentsfitness = []  # 부모들의 fitness들의 집합 (popsize 만큼 fitness 존재)
    a = parents

    pencost = 0

    for i in range(popsize):
        a1 = a[i]
        totalcost = 0
        pcost = 0
        scost = 0
        ocost = 0
        hcost = 0
        p1cost = 0
        p2cost = 0

        ss = []
        ss1 = []

        lot_size = a1[0]
        k1 = a1[1]
        k2 = a1[2]
        k3 = a1[3]
        k4 = a1[4]
        m1 = a1[5]
        m2 = a1[6]
        m3 = a1[7]
        m4 = a1[8]
        safetystock = a1[9]

        pcost = productioncost[0] * (k1[0] + k1[1]) * lot_size[0] + productioncost[1] * (k2[0] + k2[1] + k2[2]) * \
                lot_size[1] + productioncost[2] * (k3[0] + k3[1] + k3[2] + k3[3]) * lot_size[2] + productioncost[3] * (
                        k4[0] + k4[1] + k4[2] + k4[3]) * lot_size[3]
        scost = setupcost[0] * (k1[0] + k1[1]) + setupcost[1] * (k2[0] + k2[1] + k2[2]) + setupcost[2] * (
                k3[0] + k3[1] + k3[2] + k3[3]) + setupcost[3] * (k4[0] + k4[1] + k4[2] + k4[3])
        ocost = ordercost[0] * (m1[0] + m1[1]) + ordercost[1] * (m2[0] + m2[1] + m2[2] + m2[3] + m2[4] + m2[5]) + \
                ordercost[2] * (m3[0] + m3[1] + m3[2] + m3[3] + m3[4] + m3[5] + m3[6] + m3[7]) + ordercost[3] * (
                        m4[0] + m4[1])
        hcost = 2 * holdcost[0] * (coil_inventory[0] + coil_inventory[1]) + lot_size[0] * (
                k1[0] + k1[1] - m1[0] - m1[1]) + 2 * holdcost[
                    1] * (blk_inventory[0] + blk_inventory[1] + blk_inventory[2]) + lot_size[1] * (
                        k2[0] + k2[1] + k2[2] - (m2[0] + m2[1] + m2[2] + m2[3] + m2[4] + m2[5])) + 2 * \
                holdcost[2] * (prs_inventory[0] + prs_inventory[1] + prs_inventory[2] + prs_inventory[3]) + lot_size[
                    2] * (k3[0] + k3[1] + k3[2] + k3[3] - (
                m3[0] + m3[1] + m3[2] + m3[3] + m3[4] + m3[5] + m3[6] + m3[7])) + 2 * holdcost[3] * (
                        asy_inventory[0] + asy_inventory[1]) + lot_size[3] * (
                        k4[0] + k4[1] + k4[2] + k4[3] - m4[0] - m4[1])

        totalcost = 1 / (pcost + scost + ocost + hcost + p1cost + p2cost)

        parentsfitness.append(totalcost)

    return a, parentsfitness

#aa = inifs(popsize)


#print(fitness(aa,popsize))
#print("aa" , aa)

def survive(parents, popsize):
    d1 = []
    d2 = []
    a, b = fitness(parents, popsize)
    a1 = copy.deepcopy(a) # solution
    b1 = copy.deepcopy(b) # fitness 값
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(10):
        c = b1.index(b[i])  # 높은 수치를 가진 해의 index 저장
        d1.append(a1[c])
    q = inifs(initial(10))
    for j in range(10):
        qq = q[j]
        d1.append(qq)

    return d1


#bb = survive(aa, popsize)


#print(bb)

def crossover(parents, popsize):
    d1 = []
    d2 = []

    aaa = survive(parents, popsize)
    a = randrange(1, 4)
    p = randrange(0, popsize - 1)
    p1 = randrange(0, popsize - 1)
    if p == p1:
        p1 = randrange(0, popsize - 1)

    a1 = aaa.pop(p)  # 부모해 2개 가져옴
    a2 = aaa.pop(p1)

    aa1 = copy.deepcopy(a1)
    aa2 = copy.deepcopy(a2)

    lot_size = aa1[0]
    k1 = aa1[1]
    k2 = aa1[2]
    k3 = aa1[3]
    k4 = aa1[4]
    m1 = aa1[5]
    m2 = aa1[6]
    m3 = aa1[7]
    m4 = aa1[8]
    safetystock = aa1[9]

    lot_size1 = aa2[0]
    k11 = aa2[1]
    k21 = aa2[2]
    k31 = aa2[3]
    k41 = aa2[4]
    m11 = aa2[5]
    m21 = aa2[6]
    m31 = aa2[7]
    m41 = aa2[8]
    safetystock1 = aa2[9]

    off1_lot = []
    off1_k1 = []
    off1_k2 = []
    off1_k3 = []
    off1_k4 = []
    off1_m1 = []
    off1_m2 = []
    off1_m3 = []
    off1_m4 = []
    off1_ss = []

    off2_lot = []
    off2_k1 = []
    off2_k2 = []
    off2_k3 = []
    off2_k4 = []
    off2_m1 = []
    off2_m2 = []
    off2_m3 = []
    off2_m4 = []
    off2_ss = []

    ra = lot_size[1] / lot_size[2]
    ra1 = lot_size1[1] / lot_size1[2]
    if a == 3:
        if lot_size[2] >= lot_size1[3]:
            off1_lot = lot_size[:a] + lot_size1[a:]
        else:
            off1_lot = lot_size
            off1_lot[3] = off1_lot[2]

        if lot_size1[2] >= lot_size[3]:
            off2_lot = lot_size1[:a] + lot_size[a:]
        else:
            off2_lot = lot_size1
            off2_lot[3] = off2_lot[2]

    elif a == 2:
        if lot_size[1] >= lot_size1[2]:
            off1_lot = lot_size[:a] + lot_size1[a:]
        else:
            off1_lot = lot_size
            off1_lot[2] = off1_lot[1]

        if lot_size1[1] >= lot_size[2]:
            off2_lot = lot_size1[:a] + lot_size[a:]
        else:
            off2_lot = lot_size1
            off2_lot[2] = off2_lot[1]

    else:
        if lot_size[1] >= lot_size1[2]:
            off1_lot = lot_size[:a] + lot_size1[a:]
        else:
            off1_lot = lot_size
            off1_lot[2] = off1_lot[1]
        off1_lot[0] = off1_lot[1] / 500
        if lot_size1[1] >= lot_size[2]:
            off2_lot = lot_size1[:a] + lot_size[a:]
        else:
            off2_lot = lot_size1
            off2_lot[2] = off2_lot[1]
        off2_lot[0] = off2_lot[1] / 500

    if int(off1_lot[1] / 500) == off1_lot[1] / 500:
        off1_lot[1] = off1_lot[1]
    else:
        off1_lot[1] = (int(off1_lot[1] / 500) + 1) * 500

    if int(off1_lot[1] / off1_lot[2]) == off1_lot[1] / off1_lot[2]:
        off1_lot[2] = off1_lot[2]
    else:
        if int(off1_lot[1] / ra) == off1_lot[1] / ra:
            off1_lot[2] = off1_lot[1] / ra
            if off1_lot[2] % 10 != 0:
                off1_lot[2] = off1_lot[1] / ra * 2
        else:
            while True:
                ra += 1
                off1_lot[2] = off1_lot[1] / ra
                if int(off1_lot1[1] / off1_lot[2]) == off1_lot[1] / off1_lot[2]:
                    off1_lot[2] = off1_lot[2]
                    if off1_lot[2] % 10 != 0:
                        continue
                    else:
                        break

    if int(off1_lot[2] / off1_lot[3]) == off1_lot[2] / off1_lot[3]:
        off1_lot[3] = off1_lot[3]
    else:
        for z in range(100, 9, -10):
            if int(off1_lot[2] / z) == off1_lot[2] / z:
                off1_lot[3] = z
                break

    if int(off2_lot[1] / 500) == off2_lot[1] / 500:
        off2_lot[1] = off2_lot[1]
    else:
        off2_lot[1] = (int(off2_lot[1] / 500) + 1) * 500

    if int(off2_lot[1] / off2_lot[2]) == off2_lot[1] / off2_lot[2]:
        off2_lot[2] = off2_lot[2]
    else:
        if int(off2_lot[1] / ra1) == off2_lot[1] / ra1:
            off2_lot[2] = off2_lot[1] / ra1
            if off2_lot[2] % 10 != 0:
                off2_lot[2] = off2_lot[1] / ra1 * 2
        else:
            while True:
                ra1 += 1
                off2_lot[2] = off2_lot[1] / ra1
                if int(off2_lot[1] / off2_lot[2]) == off2_lot[1] / off2_lot[2]:
                    off2_lot[2] = off2_lot[2]
                    if off2_lot[2] % 10 != 0:
                        continue
                    else:
                        break

    if int(off2_lot[2] / off2_lot[3]) == off2_lot[2] / off2_lot[3]:
        off2_lot[3] = off2_lot[3]
    else:
        for z in range(100, 9, -10):
            if int(off2_lot[2] / z) == off2_lot[2] / z:
                off2_lot[3] = z
                break

    off1_ss = safetystock
    off1_k1 = k1
    off1_k2 = k2
    off1_k3 = k3
    off1_k4 = k4
    off1_m1 = m1
    off1_m2 = m2
    off1_m3 = m3
    off1_m4 = m4

    off2_k1 = k11
    off2_k2 = k21
    off2_k3 = k31
    off2_k4 = k41
    off2_m1 = m11
    off2_m2 = m21
    off2_m3 = m31
    off2_m4 = m41
    off2_ss = safetystock1

    d1.append(off1_lot)
    d1.append(off1_k1)
    d1.append(off1_k2)
    d1.append(off1_k3)
    d1.append(off1_k4)
    d1.append(off1_m1)
    d1.append(off1_m2)
    d1.append(off1_m3)
    d1.append(off1_m4)
    d1.append(off1_ss)

    d2.append(off2_lot)
    d2.append(off2_k1)
    d2.append(off2_k2)
    d2.append(off2_k3)
    d2.append(off2_k4)
    d2.append(off2_m1)
    d2.append(off2_m2)
    d2.append(off2_m3)
    d2.append(off2_m4)
    d2.append(off2_ss)

    aaa.append(d1)
    aaa.append(d2)
    parents = aaa
    return parents


# crossover 사용할지 고민 해보기 ..
# 사용 한다면 끝나고 inifs(parents)를 통해 feasible로 만들어야 된다.

#cc = crossover(bb, popsize)

#dd = inifs(cc)


#print(cc)

def inifs1(parents):
    a = parents
    for i in range(len(a)):
        pencost = 0
        lot_size = []
        k1 = []
        k2 = []
        k3 = []
        k4 = []
        m1 = []
        m2 = []
        m3 = []
        m4 = []
        safetystock = []

        lot_size = a[i][0]
        k1 = a[i][1]
        k2 = a[i][2]
        k3 = a[i][3]
        k4 = a[i][4]
        m1 = a[i][5]
        m2 = a[i][6]
        m3 = a[i][7]
        m4 = a[i][8]
        safetystock = a[i][9]

        for j in range(len(k1)):
            if int(k1[j]) == k1[j]:
                k1[j] = k1[j]
            else:
                k1[j] = int(k1[j]) + 1

        for j in range(len(m1)):
            if int(m1[j]) == m1[j]:
                m1[j] = m1[j]
            else:
                m1[j] = int(m1[j]) + 1

        while True:
            if safetystock[0] > (coil_inventory[0] + lot_size[0] * (k1[0] - m1[0])):
                k1[0] += 1
            else:
                break

        while True:
            if safetystock[0] > (coil_inventory[1] + lot_size[1] * (k1[1] - m1[1])):
                k1[1] += 1
            else:
                break

        k2[0] = (m1[0] + safetystock[1] / lot_size[1])
        k2[1] = (m1[1] + safetystock[1] / lot_size[1])
        k2[2] = m2[2] + m2[5] + safetystock[1] / lot_size[1]
        for j in range(len(k2)):
            if int(k2[j]) == k2[j]:
                k2[j] = k2[j]
            else:
                k2[j] = int(k2[j])

        for j in range(len(m2)):
            if int(m2[j]) == m2[j]:
                m2[j] = m2[j]
            else:
                m2[j] = int(m2[j]) + 1

        while True:
            if safetystock[1] > blk_inventory[0] + lot_size[1] * (k2[0] - m2[1] - m2[4]):
                k2[0] += 1
            else:
                break

        while True:
            if safetystock[1] > blk_inventory[1] + lot_size[1] * (k2[1] - m2[0] - m2[3]):
                k2[1] += 1
            else:
                break

        while True:
            if safetystock[1] > blk_inventory[2] + lot_size[1] * (k2[2] - m2[2] - m2[5]):
                k2[2] += 1
            else:
                break

        k3[0] = (m2[0] + safetystock[2] / lot_size[2])
        k3[1] = (m2[1] + safetystock[2] / lot_size[2])
        k3[2] = (m2[2] + safetystock[2] / lot_size[2])
        k3[3] = m3[0] + m3[4] + safetystock[2] / lot_size[2]
        for j in range(len(k3)):
            if int(k3[j]) == k3[j]:
                k3[j] = k3[j]
            else:
                k3[j] = int(k3[j]) + 1

        m3[4] = prs_demand[0] / lot_size[2]
        m3[5] = prs_demand[1] / lot_size[2]
        m3[6] = prs_demand[2] / lot_size[2]
        m3[7] = prs_demand[3] / lot_size[2]
        for j in range(len(m3)):
            if int(m3[j]) == m3[j]:
                m3[j] = m3[j]
            else:
                m3[j] = int(m3[j]) + 1

        while True:
            if safetystock[2] > prs_inventory[0] + lot_size[2] * (k3[0] - m3[2] - m3[6]):
                k3[0] += 1
            else:
                break

        while True:
            if safetystock[2] > prs_inventory[1] + lot_size[2] * (k3[1] - m3[1] - m3[5]):
                k3[1] += 1
            else:
                break

        while True:
            if safetystock[2] > prs_inventory[2] + lot_size[2] * (k3[2] - m3[3] - m3[7]):
                k3[2] += 1
            else:
                break

        while True:
            if safetystock[2] > prs_inventory[3] + lot_size[2] * (k3[3] - m3[0] - m3[4]):
                k3[3] += 1
            else:
                break

        k4[0] = m3[0] + safetystock[3] / lot_size[3]
        k4[1] = m3[1] + safetystock[3] / lot_size[3]
        k4[2] = m3[2] + safetystock[3] / lot_size[3]
        k4[3] = m3[3] + safetystock[3] / lot_size[3]

        if k4[0] >= k4[1]:
            k4[0] = k4[1]
        else:
            k4[1] = k4[0]

        if k4[2] >= k4[3]:
            k4[2] = k4[3]
        else:
            k4[3] = k4[2]

        for j in range(len(k4)):
            if int(k4[j]) == k4[j]:
                k4[j] = k4[j]
            else:
                k4[j] = int(k4[j]) + 1

        if asy_inventory[0] >= asy_demand[0] + safetystock[3] :
            m4[0] = 0
        else :
            m4[0] = asy_demand[0] / lot_size[3]

        if asy_inventory[1] >= asy_demand[1] + safetystock[3] :
            m4[1] = 0
        else :
            m4[1] = asy_demand[1] / lot_size[3]

        for j in range(len(m4)):
            if int(m4[j]) == m4[j]:
                m4[j] = m4[j]
            else:
                m4[j] = int(m4[j]) + 1

        if asy_inventory[0] - (asy_demand[0] - m4[0] * lot_size[3]) >= 0:
            m4[0] = asy_demand[0] / lot_size[3]
        else:
            m4[0] = 0

        if asy_inventory[1] - (asy_demand[1] - m4[1] * lot_size[3]) >= 0:
            m4[1] = asy_demand[1] / lot_size[3]
        else:
            m4[1] = 0

        for j in range(len(m4)):
            if int(m4[j]) == m4[j]:
                m4[j] = m4[j]
            else:
                m4[j] = int(m4[j]) + 1

        if asy_inventory[0] - (asy_demand[0] - m4[0] * lot_size[3]) >= 0 :
            k4[0] = 0
            k4[1] = k4[0]

        if asy_inventory[1] - (asy_demand[1] - m4[1] * lot_size[3]) >= 0:
            k4[2] = 0
            k4[3] = k4[2]

        while True:
            if safetystock[3] > asy_inventory[0] + lot_size[3] * (k4[0] - m4[0]):
                k4[0] += 1
                k4[1] = k4[0]
            else:
                break

        while True:
            if safetystock[3] > asy_inventory[1] + lot_size[3] * (k4[2] - m4[1]):
                k4[2] += 1
                k4[3] = k4[2]
            else:
                break

        c = asy_demand[0] - asy_inventory[0] + safetystock[3]  # 앞 공정에서 c만큼 생산되어야 함
        d = asy_demand[1] - asy_inventory[1] + safetystock[3]  # 앞 공정에서 d만큼 생산되어야 함

        #z = gcd(c, d)  # z 는 asy demand들의 최대 공약수
        z = randrange(10,101,10)

        a1 = m4[0] * z
        a2 = m4[1] * z

        #a3 = gcd(a1, a2)  # m3*Q로 보내질 양은 미리 정해져 있음 ..  그것의 공약수로 로트 결정
        #a3 = randrange(10,100,1)
        """
        if int(lot_size[2] / z) == lot_size[2] / z :
            lot_size[3] = z
        else :
            for i in range(int(lot_size[2] / z) + 1, 11, -1):
                if int(lot_size[2] / i) == lot_size[2] / i:
                    lot_size[3] = lot_size[2] / i
                    break

        if a3 >= lot_size[3]:
            a3 = a3
        else:
            a3 = lot_size[3]
        """

        k4[0] = c / lot_size[3]
        k4[1] = k4[0]
        k4[2] = d / lot_size[3]
        k4[3] = k4[2]

        for i in range(len(k4)):
            if int(k4[i]) == k4[i]:
                k4[i] = k4[i]
            else:
                k4[i] = int(k4[i]) + 1

        m3[0] = k4[0] * lot_size[3] / lot_size[2]
        m3[1] = k4[1] * lot_size[3] / lot_size[2]
        m3[2] = k4[2] * lot_size[3] / lot_size[2]
        m3[3] = k4[3] * lot_size[3] / lot_size[2]
        m3[4] = prs_demand[0] / lot_size[2]
        m3[5] = prs_demand[1] / lot_size[2]
        m3[6] = prs_demand[2] / lot_size[2]
        m3[7] = prs_demand[3] / lot_size[2]

        for i in range(len(m3)):
            if int(m3[i]) == m3[i]:
                m3[i] = m3[i]
            else:
                m3[i] = int(m3[i]) + 1

        k4[0] = m3[0] * lot_size[2] / lot_size[3]
        k4[1] = k4[0]
        k4[2] = m3[2] * lot_size[2] / lot_size[3]
        k4[3] = k4[2]

        b1 = (m3[2] + m3[6]) * lot_size[2] + safetystock[2]
        b2 = (m3[1] + m3[5]) * lot_size[2] + safetystock[2]
        b3 = (m3[3] + m3[7]) * lot_size[2] + safetystock[2]
        b4 = (m3[0] + m3[4]) * lot_size[2] + safetystock[2]

        m2[0] = b1 / lot_size[1]
        m2[1] = b2 / lot_size[1]
        m2[2] = b3 / lot_size[1]
        m2[3] = blk_demand[0] / lot_size[1]
        m2[4] = blk_demand[1] / lot_size[1]
        m2[5] = blk_demand[2] / lot_size[1]

        for i in range(len(m2)):
            if int(m2[i]) == m2[i]:
                m2[i] = m2[i]
            else:
                m2[i] = int(m2[i]) + 1

        k3[0] = m3[2] + m3[6] + (safetystock[2] - prs_inventory[0]) / lot_size[2]
        k3[1] = m3[1] + m3[5] + (safetystock[2] - prs_inventory[1]) / lot_size[2]
        k3[2] = m3[3] + m3[7] + (safetystock[2] - prs_inventory[2]) / lot_size[2]
        k3[3] = m3[0] + m3[4] + (safetystock[2] - prs_inventory[3]) / lot_size[2]
        for i in range(len(k3)):
            if int(k3[i]) == k3[i]:
                k3[i] = k3[i]
            else:
                k3[i] = int(k3[i]) + 1

        m2[0] = k3[0] * lot_size[2] / lot_size[1]
        m2[1] = k3[1] * lot_size[2] / lot_size[1]
        m2[2] = k3[2] * lot_size[2] / lot_size[1]
        for i in range(len(m2)):
            if int(m2[i]) == m2[i]:
                m2[i] = m2[i]
            else:
                m2[i] = int(m2[i]) + 1
        k3[0] = m2[0] * lot_size[1] / lot_size[2]
        k3[1] = m2[1] * lot_size[1] / lot_size[2]
        k3[2] = m2[2] * lot_size[1] / lot_size[2]
        for i in range(len(k2)):
            if int(k2[i]) == k2[i]:
                k2[i] = k2[i]
            else:
                k2[i] = int(k2[i]) + 1

        k2[0] = m2[1] + m2[4] + (safetystock[1] - blk_inventory[0]) / lot_size[1]
        k2[1] = m2[0] + m2[3] + (safetystock[1] - blk_inventory[1]) / lot_size[1]
        k2[2] = m2[2] + m2[5] + (safetystock[1] - blk_inventory[2]) / lot_size[1]
        for i in range(len(k2)):
            if int(k2[i]) == k2[i]:
                k2[i] = k2[i]
            else:
                k2[i] = int(k2[i]) + 1

        m1[0] = k2[0]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생
        m1[1] = k2[1]  # 500 개씩 나온다는 이퀄 제약으로 인해 발생

        k1[0] = m1[0] + (safetystock[0] - coil_inventory[0]) / lot_size[0]
        k1[1] = m1[1] + (safetystock[0] - coil_inventory[1]) / lot_size[0]

        for i in range(len(k1)):
            if int(k1[i]) == k1[i]:
                k1[i] = k1[i]
            else:
                k1[i] = int(k1[i]) + 1

        for i in range(len(k2)):
            if int(k2[i]) == k2[i]:
                k2[i] = k2[i]
            else:
                k2[i] = int(k2[i]) + 1

        for i in range(len(k3)):
            if int(k3[i]) == k3[i]:
                k3[i] = k3[i]
            else:
                k3[i] = int(k3[i]) + 1

        for i in range(len(k4)):
            if int(k4[i]) == k4[i]:
                k4[i] = k4[i]
            else:
                k4[i] = int(k4[i])  # + 1

        for i in range(len(m1)):
            if int(m1[i]) == m1[i]:
                m1[i] = m1[i]
            else:
                m1[i] = int(m1[i]) + 1

        for i in range(len(m3)):
            if int(m3[i]) == m3[i]:
                m3[i] = m3[i]
            else:
                m3[i] = int(m3[i]) + 1

        for i in range(len(m4)):
            if int(m4[i]) == m4[i]:
                m4[i] = m4[i]
            else:
                m4[i] = int(m4[i]) + 1

        for i in range(len(m4)):
            if int(m4[i]) == m4[i]:
                m4[i] = m4[i]
            else:
                m4[i] = int(m4[i]) + 1

        if k1[0] <= 0:
            k1[0] = 0
        if k1[1] <= 0:
            k1[1] = 0

    return a


#ff = inifs1(ee)
#print(ff)

def mutation(parents):
    """
    초기해 가져오는 부분 작성해야 됨..
    if 문 안에 넣은 것들은 .. lot를 줄여가면서 해가 좋아지나 보는 방법임
    lot를 크게 하면서 해가 좋아지나 보는 것은 하지 않았음 ..
    """
    prob = randrange(0, 1)
    aa = crossover(cc, popsize)
    qqq = inifs(aa)
    local = []
    local1 = []

    if prob <= 1:

        rd = randrange(0, popsize, 1)  # population 중에 1개의 해를 random으로 선택한다.

        aaa = qqq[rd]  # crossover 가 끝난 parents 중에서 1개의 해를 결정
        qqq.remove(aaa)

        lot_size = aaa[0]
        k1 = aaa[1]
        k2 = aaa[2]
        k3 = aaa[3]
        k4 = aaa[4]
        m1 = aaa[5]
        m2 = aaa[6]
        m3 = aaa[7]
        m4 = aaa[8]
        safetystock = aaa[9]

        a = randrange(0, len(parents), 1)  # mutation을 진행 할 solution을 하나 뽑는다.
        b = randrange(1, 4, 1)  # 어느 lot를 변경 시킬지 뽑기...
        #b = 2

        if b == 1:
            c = []  # lotsize2로 나눴을때 0 이 나오는 것 모으는 용도
            e = []
            aaaa = copy.deepcopy(aaa)
            for i in range(1, lot_size[1] + 1):
                if int(i / lot_size[2]) == i / lot_size[2]:
                    if int(i / 500) == i / 500 :
                        c.append(i)
            for i in range(len(c)):
                if int(lot_size[1] / lot_size[2]) == lot_size[1] / lot_size[2]:
                    lot_size[1] = lot_size[1]
                    b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                    lot_size[1] = b1
                    lot_size[0] = lot_size[1] / 500
                    c1 = copy.deepcopy(lot_size)
                    aaaa[0] = c1
                    d1 = copy.deepcopy(aaaa)
                    local1.append(d1)
                else:
                    while True:
                        # e = randrange(0, len(c), 1)
                        # lot_size[2] = c[e]
                        if int(lot_size[1] / lot_size[2]) == lot_size[1] / lot_size[2]:
                            b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                            c1 = copy.deepcopy(lot_size)
                            aaaa[0] = c1
                            lot_size[0] = lot_size[1] / 500
                            d1 = copy.deepcopy(aaaa)
                            local1.append(d1)
                            break
                        else:
                            break

        elif b == 2:
            c = []
            e = []
            aaaa = copy.deepcopy(aaa)
            for i in range(int(lot_size[3]), lot_size[1]+1, int(lot_size[3])):
                if int(lot_size[1] / i) == lot_size[1] / i:
                    if int(lot_size[2] / lot_size[3]) == lot_size[2] / lot_size[3] :
                        c.append(i)
            for i in range(len(c)):
                if int(lot_size[1] / lot_size[2]) == lot_size[1] / lot_size[2]:
                    if int(lot_size[2] / lot_size[3] ) == lot_size[2] / lot_size[3] :
                        lot_size[2] = lot_size[2]
                        b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                        lot_size[2] = b1
                        c1 = copy.deepcopy(lot_size)
                        aaaa[0] = c1
                        d1 = copy.deepcopy(aaaa)
                        local1.append(d1)
                    else :
                        for i in range(10, 101, 10):
                            if int(lot_size[2] / i) == lot_size[2] / i:
                                lot_size[3] = i
                                break
                else:
                    while True:
                        # e = randrange(0, len(c), 1)
                        # lot_size[2] = c[e]
                        if int(lot_size[1] / lot_size[2]) == lot_size[1] / lot_size[2]:
                            if int(lot_size[2] / lot_size[3] ) == lot_size[2] / lot_size[3] :
                                b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                                lot_size[2] = b1
                                c1 = copy.deepcopy(lot_size)
                                aaaa[0] = c1
                                d1 = copy.deepcopy(aaaa)
                                local1.append(d1)
                                break
                            else :
                                for i in range(10, 101, 10):
                                    if int(lot_size[2] / i) == lot_size[2] / i:
                                        lot_size[3] = i
                                        break
                                b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                                lot_size[2] = b1
                                c1 = copy.deepcopy(lot_size)
                                aaaa[0] = c1
                                d1 = copy.deepcopy(aaaa)
                                local1.append(d1)
                                break
                        else:
                            break

        elif b == 3:
            c = []
            e = []
            aaaa = copy.deepcopy(aaa)
            for i in range(10, 101, 10):
                if lot_size[2] % i == 0:
                    c.append(i)
            for i in range(len(c)):
                lot_size[3] = c[i]
                if int(lot_size[2] / lot_size[3]) == lot_size[2] / lot_size[3]:
                    lot_size[3] = lot_size[3]
                    b1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                    lot_size[3] = b1
                    c1 = copy.deepcopy(lot_size)
                    aaaa[0] = c1
                    d1 = copy.deepcopy(aaaa)
                    local1.append(d1)
                else:  # lot_size[2] 와 lot_size[3] 의 관계가 소숫점이 남으면 정수해 만드는데 제약이 생긴다.
                    while True:
                        if int(lot_size[2] / lot_size[3]) == lot_size[2] / lot_size[3]:
                            bb1 = copy.deepcopy(c[i])  # c[i] 순서대로 넣어보기 ..
                            lot_size[3] = bb1
                            c1 = copy.deepcopy(lot_size)
                            aaaa[0] = c1
                            d1 = copy.deepcopy(aaaa)
                            local1.append(d1)
                            break
                        else:
                            break

        lo = inifs1(local1)

        """
        여기서 좋은 해가 추가 되는 것 추가하기 .. 
        """
        a1, a2 = fitness(lo, len(lo))  # a1에는 parents 가  a2에는 fitness 가 들어옴
        point = max(a2)
        p1 = a2.index(point)
        qqq.append(a1[p1])

#    else:
#        qqq = qqq

    return qqq

#ee = mutation(bb)
#print(ee)

"""
inifs 는 초기해 생성 후 초기해의 feasible 체크를 위한 용도 (popsize가 인자)
inifs1 은 반복 과정에서 crossover나 mutation 진행 후 feasible 체크를 위한 용도 (parents가 인자)
"""


"""
mutation 끝나고 fitness 진행 후 terminate 하던지 반복하던지 진행 ... 
"""

"""
반복문 통해 좋은해 찾기 .. 
"""


count1 = 0
maxcount = 0
fitsave = [0]
same = 0

maxsolution = [0]

aa = inifs(initial(popsize))
bb1, bb2 = fitness(aa, popsize)  # bb1 : parents , bb2 : fitness 값


while True:
    for i in range(3000):
        if count1 == 3000:  # 500번 반복후 종료
            print("500번 generation 종료")
            break

        cc = survive(bb1, popsize)
        dd = crossover(cc, popsize)
        ee = inifs1(dd)
        ff = mutation(ee)
        hh1, hh2 = fitness(ff, popsize)

        maxindex = hh2.index(max(hh2))  # 20개씩 생성된 해들 중에서 제일 좋은 값의 위치를 뽑아내는 코드
        # maxsolution.append(hh1[maxindex])

        print(maxsolution)
        print("hh : ", max(hh2))
        if max(fitsave) <= max(hh2):
            maxsolution.append(hh1[maxindex])
            fitsave.append(max(hh2))
        if fitsave.count(max(fitsave)) == 10:  # maxsolution이 아닌 fitness로 비교해야 한다..
            print("동일한 해 10번으로 인해 종료")
            break
        count1 += 1
        bb1 = hh1
    print("count에서 종료 : ", count1)
    break

print("걸린 시간은 : ", time.time() - start_time)

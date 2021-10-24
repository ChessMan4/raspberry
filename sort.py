import random
import timeit
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

cisla = [random.uniform(0, 1000) for i in range(0, 10000)]


def bubble(cisla):

    n = len(cisla)

    flag = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if cisla[j] > cisla[j + 1]:
                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
                flag = 1
        if flag == 0:
            break

def select(cisla):
    n = len(cisla)

    for i in range(n):
        x = i
        for j in range(i + 1, n):
            if cisla[x] > cisla[j]:
                x = j

        cisla[i], cisla[x] = cisla[x], cisla[i]


def merge(cisla):
    if len(cisla) > 1:
        pul = len(cisla) // 2
        leva = cisla[:pul]
        prava = cisla[pul:]

        merge(leva)
        merge(prava)

        i = j = k = 0

        while i < len(leva) and j < len(prava):
            if leva[i] < prava[j]:
                cisla[k] = leva[i]
                i += 1
            else:
                cisla[k] = prava[j]
                j += 1
            k += 1

        while i < len(leva):
            cisla[k] = leva[i]
            i += 1
            k += 1

        while j < len(prava):
            cisla[k] = prava[j]
            j += 1
            k += 1


#cisla = [10, 105, 1055, 1, 8]
bubbletime = []
selecttime = []
mergetime = []

for i in range(100):
    cisla = [random.uniform(0, 1000) for i in range(0, 100000)]
    start_time1 = timeit.default_timer()
    bubble(cisla)
    stop_time1 = timeit.default_timer() - start_time1
    print(i)
    bubbletime.append(stop_time1)

for j in range(100):
    cisla = [random.uniform(0, 1000) for i in range(0, 100000)]
    start_time2 = timeit.default_timer()
    select(cisla)
    stop_time2 = timeit.default_timer() - start_time2
    print(j)
    selecttime.append(stop_time2)

for k in range(100):
    cisla = [random.uniform(0, 1000) for i in range(0, 100000)]
    start_time3 = timeit.default_timer()
    select(cisla)
    stop_time3 = timeit.default_timer() - start_time3
    print(k)
    mergetime.append(stop_time3)

bubbleaverage = mean(bubbletime)
selectaverage = mean(selecttime)
mergeaverage = mean(mergetime)

print(mergeaverage)

x = np.arange(3)
plt.bar(x, height=[bubbleaverage,selectaverage,mergeaverage])
plt.xticks(x, ['BubbleSort',"SelectSort", "MergeSort"]);
plt.ylabel("Time [s]")
plt.show()

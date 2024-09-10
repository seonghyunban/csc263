import math
import numpy as np


def parent(i):
    return math.floor((i - 1) / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class MaxHeap:
    def __init__(self):
        self.A = []
        self.size = 0

    def __str__(self):
        return self.A.__str__()

    def Max(self):
        return self.A[0]

    def Max_Heapify(self, i):
        l = left(i)
        r = right(i)

        if l < self.size and self.A[l] > self.A[i]:
            lrg = l
        else:
            lrg = i
        if r < self.size and self.A[r] > self.A[lrg]:
            lrg = r

        if lrg != i:
            self.A[i] , self.A[lrg] = self.A[lrg], self.A[i]
            self.Max_Heapify(lrg)

    def Insert(self, x):
        i = self.size

        self.A.append(x)
        self.size += 1
        p = parent(i)

        while i > 0 and self.A[i] > self.A[p]:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p = parent(i)

    def Extract_Max(self):
        if self.size < 1:
            print("Error:: Extract_Max from empty MaxHeap")
        maxi = self.Max()
        self.A[0] = self.A[self.size - 1]
        self.A.pop()
        self.size -= 1
        self.Max_Heapify(0)
        return maxi


class MinHeap:
    def __init__(self):
        self.A = []
        self.size = 0

    def __str__(self):
        return self.A.__str__()

    def Min(self):
        return self.A[0]

    def Min_Heapify(self, i):
        l = left(i)
        r = right(i)

        if l < self.size and self.A[l] < self.A[i]:
            sml = l
        else:
            sml = i
        if r < self.size and self.A[r] < self.A[sml]:
            sml = r

        if sml != i:
            self.A[i], self.A[sml] = self.A[sml], self.A[i]
            self.Min_Heapify(sml)

    def Insert(self, x):
        i = self.size

        self.A.append(x)
        self.size += 1
        p = parent(i)

        while i > 0 and self.A[i] < self.A[p]:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p = parent(i)

    def Extract_Min(self):
        if self.size < 1:
            print("Error:: Extract_Min from empty MaxHeap")
        mini = self.Min()

        self.A[0] = self.A[self.size - 1]
        self.A.pop()
        self.size -= 1
        self.Min_Heapify(0)
        return mini


def Extract_Median(A: list):
    lower = MaxHeap()
    upper = MinHeap()
    n = len(A)

    if n < 2:
        return A

    meds = [A[0], (A[0] + A[1]) / 2]

    if A[0] <= A[1]:
        lower.Insert(A[0])
        upper.Insert(A[1])
    else:
        lower.Insert(A[1])
        upper.Insert(A[0])

    for i in range(2, n):
        if i % 2 == 0:
            if A[i] >= upper.Min():
                lower.Insert(upper.Extract_Min())
                upper.Insert(A[i])
            else:
                lower.Insert(A[i])
            meds.append(lower.Max())
        else:
            if A[i] <= lower.Max():
                upper.Insert(lower.Extract_Max())
                lower.Insert(A[i])
            else:
                upper.Insert(A[i])
            meds.append((lower.Max() + upper.Min()) / 2)

    return meds


def answer(A):
    meds = []
    for i in range(len(A)):
        cur = A[:i + 1]
        cur.sort()
        if i % 2 == 0:
            meds.append(cur[i // 2])
        else:
            a = i // 2
            b = i // 2 + 1
            meds.append((cur[a] + cur[b]) / 2)
    return meds

test = [1, 2, 3, 4, 5, 6, 7, 8, 9]


exp = answer(test)
rslt = Extract_Median(test)

print(exp)
print(rslt)










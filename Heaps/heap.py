

import heapq


A = [-4, 3, 1, 0, 2, 5, 8, 12, 9]

# build a heap
heapq.heapify(A)

# heap push
# o(log(n))
# insert an element to a heap
heapq.heappush(A,4)

# heap pop min
# o(log(n))
min = heapq.heappop(A)

# heap push pop - removes root and adds element to heap
heapq.heappushpop(A, 99)


# heap sort
# time: o(n log n) space: o(n)
# NB: O(1) is possible but complex
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)

    sort_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        sort_list[i] = minn

    return sort_list

'''
    ====================================================

    For max heap functionalities, just negate the values as in min heap

    ====================================================

'''


# Adding tuples to heaps for leetcode and neetcode questions
from collections import Counter

A = [ 5,6,8,4,3,6,5,5,4,1 ] 

counter = Counter(A)
# loop through values

for k, v in counter.items():
    print(k, v)

heap = []

for k, v in counter.items():
    heapq.heappush(heap, (k,v))

print(heap)

from itertools import product
from time import time
count = 0
numbers = []
n, k = map(int, input().split())
numbers = [int(el) for el in input().split()]
ans = []
min_max = sum(numbers)
splits = [1 for i in range(k - 1)] + [n - k + 1]
for splits in product(range(n), repeat=k):
    if sum(splits) == n:
        count += 1
        variant = []
        start = 0
        for lim in splits:
            variant.append(numbers[start:start+lim])
            start += lim
        cur_max = max(sum(v) for v in variant)
        if cur_max == min_max:
            ans.append(splits)
        elif cur_max < min_max:
            min_max = cur_max
            ans = [splits]
for a in ans:
    # print(a)
    for i in range(len(a)-1):
        print(sum(a[0:i+1]), end=' ')
    print()

